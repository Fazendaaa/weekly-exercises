# import errno
# import os
# from unittest.mock import ANY, NonCallableMagicMock, call, patch
#
# import pytest
#
# from test_utils import MockSock, MockFile, MockException, ZEN, SuperMock
# from paasio import MeteredFile, MeteredSocket
#
#
# class TestPaasio:
#     def test_meteredsocket_context_manager(self):
#         wrapped = MockSock()
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         mock.__exit__.side_effect = wrapped.__exit__
#         with MeteredSocket(mock) as socket:
#             assert not mock.__enter__.called
#             socket.recv(30)
#         assert not mock.__enter__.called
#         mock.__exit__.assert_called_once_with(None, None, None)
#         assert len(mock.mock_calls) == 2
#         with pytest.raises(OSError, match=os.strerror(errno.EBADF)):
#             socket.recv(30)
#         with pytest.raises(OSError, match=os.strerror(errno.EBADF)):
#             socket.send(b"")
#
#     def test_meteredsocket_context_manager_exception_raise(self):
#         exception = MockException("Should raise")
#         wrapped = MockSock(exception=exception)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         mock.__exit__.side_effect = wrapped.__exit__
#         with pytest.raises(MockException, match="Should raise") as err:
#             with MeteredSocket(mock) as socket:
#                 assert not mock.__enter__.called
#                 socket.recv(4096)
#         assert not mock.__enter__.called
#         mock.__exit__.assert_called_once_with(
#             MockException,
#             err.value,
#             ANY,
#         )
#         assert exception == err.value
#
#     def test_meteredsocket_context_manager_exception_suppress(self):
#         exception = MockException("Should suppress")
#         wrapped = MockSock(exception=exception)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         mock.__exit__.side_effect = wrapped.__exit__
#         with MeteredSocket(mock) as socket:
#             assert not mock.__enter__.called
#             socket.recv(4096)
#         assert not mock.__enter__.called
#         mock.__exit__.assert_called_once_with(
#             MockException,
#             exception,
#             ANY,
#         )
#
#     def test_meteredsocket_recv_once(self):
#         mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
#         with MeteredSocket(mock) as socket:
#             actual_recv = socket.recv(4096)
#         assert ZEN == actual_recv
#         assert socket.recv_ops == 1
#         assert socket.recv_bytes == len(ZEN)
#         assert mock.recv.call_count == 1
#
#     def test_meteredsocket_recv_multiple(self):
#         wrapped = MockSock()
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         actual_recv = b""
#         with MeteredSocket(mock) as socket:
#             for _ in range(5):
#                 actual_recv += socket.recv(30)
#         assert actual_recv == ZEN[:150]
#         assert socket.recv_ops == 5
#         assert socket.recv_bytes == 150
#         assert mock.recv.call_count == 5
#
#     def test_meteredsocket_recv_multiple_chunk(self):
#         wrapped = MockSock(chunk=20)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         actual_recv = b""
#         with MeteredSocket(mock) as socket:
#             for _ in range(5):
#                 actual_recv += socket.recv(4096)
#             actual_recv += socket.recv(10)
#         assert actual_recv == ZEN[:110]
#         assert socket.recv_ops == 6
#         assert socket.recv_bytes == 110
#         assert mock.recv.call_count == 6
#
#     def test_meteredsocket_recv_under_size(self):
#         wrapped = MockSock(chunk=257)  # largish odd number
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         with MeteredSocket(mock) as socket:
#             actual_recv = socket.recv(4096)
#         assert actual_recv == ZEN[:257]
#         assert socket.recv_ops == 1
#         assert socket.recv_bytes == 257
#         assert mock.recv.call_count == 1
#
#     def test_meteredsocket_send_once(self):
#         wrapped = MockSock(chunk=257)  # largish odd number
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         with MeteredSocket(mock) as socket:
#             send_len = socket.send(ZEN)
#             assert wrapped._sender.getbuffer() == ZEN[:257]
#         assert send_len == 257
#         assert socket.send_ops == 1
#         assert socket.send_bytes == 257
#         assert mock.send.call_count == 1
#
#     def test_meteredsocket_send_multiple(self):
#         wrapped = MockSock()
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         send_len = 0
#         expected = b"Tomorrow's victory is today's practice."
#         with MeteredSocket(mock) as socket:
#             send_len += socket.send(b"Tomorro")
#             send_len += socket.send(b"w's victo")
#             send_len += socket.send(b"ry is today")
#             send_len += socket.send(b"'s practice.")
#             assert wrapped._sender.getbuffer() == expected
#         assert send_len == 39
#         assert socket.send_ops == 4
#         assert socket.send_bytes == 39
#         assert mock.send.call_count == 4
#
#     def test_meteredsocket_send_under_size(self):
#         wrapped = MockSock(chunk=257)  # largish odd number
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         with MeteredSocket(mock) as socket:
#             send_len = socket.send(ZEN[:123])
#             assert wrapped._sender.getbuffer() == ZEN[:123]
#         assert send_len == 123
#         assert socket.send_ops == 1
#         assert socket.send_bytes == 123
#         assert mock.send.call_count == 1
#
#     def test_meteredsocket_bufsize_required(self):
#         mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
#         with pytest.raises(TypeError, match="argument"):
#             with MeteredSocket(mock) as socket:
#                 socket.recv()
#         assert not mock.recv.called
#
#         mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
#         with pytest.raises(TypeError, match="^'NoneType'.+integer$"):
#             with MeteredSocket(mock) as socket:
#                 socket.recv(None)
#         assert (
#             call(None) in mock.recv.mock_calls
#             or call(None, ANY) in mock.recv.mock_calls
#         )
#
#     def test_meteredsocket_flags_support(self):
#         mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
#         with MeteredSocket(mock) as socket:
#             assert socket.send(ZEN, 42) == len(ZEN)
#             assert socket.recv(4096, 24) == ZEN
#         mock.send.assert_called_once_with(ZEN, 42)
#         mock.recv.assert_called_once_with(4096, 24)
#
#         wrapped = MockSock()
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         with MeteredSocket(mock) as socket:
#             socket.recv(50)
#             assert wrapped.flags == 0
#             socket.send(b"no flags")
#             assert wrapped.flags == 0
#             socket.recv(30, 30)
#             assert wrapped.flags == 30
#             socket.send(b"flags", 1024)
#             assert wrapped.flags == 1024
#             with pytest.raises(TypeError, match="integer is required"):
#                 socket.send(b"data", None)
#             with pytest.raises(TypeError, match="integer is required"):
#                 socket.send(b"data", b"flags")
#             with pytest.raises(TypeError, match="integer is required"):
#                 socket.recv(b"data", None)
#             with pytest.raises(TypeError, match="integer is required"):
#                 socket.recv(b"data", b"flags")
#
#     def test_meteredsocket_stats_read_only(self):
#         mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
#         with MeteredSocket(mock) as socket:
#             assert socket.send_ops == 0
#             assert socket.send_bytes == 0
#             assert socket.recv_ops == 0
#             assert socket.recv_bytes == 0
#             for _ in range(277):
#                 socket.send(b"b")
#             socket.send(b"bytes")
#             for _ in range(257):
#                 socket.recv(1)
#             socket.recv(2)
#             assert socket.send_ops == 278
#             assert socket.send_bytes == 282
#             assert socket.recv_ops == 258
#             assert socket.recv_bytes == 259
#             with pytest.raises(
#                 AttributeError,
#                 match="property 'send_ops' of 'MeteredSocket' object has no setter",
#             ):
#                 socket.send_ops = 0
#             with pytest.raises(
#                 AttributeError,
#                 match="property 'send_bytes' of 'MeteredSocket' object has no setter",
#             ):
#                 socket.send_bytes = 0
#             with pytest.raises(
#                 AttributeError,
#                 match="property 'recv_ops' of 'MeteredSocket' object has no setter",
#             ):
#                 socket.recv_ops = 0
#             with pytest.raises(
#                 AttributeError,
#                 match="property 'recv_bytes' of 'MeteredSocket' object has no setter",
#             ):
#                 socket.recv_bytes = 0
#             assert socket.send_ops == 278
#             assert socket.send_bytes == 282
#             assert socket.recv_ops == 258
#             assert socket.recv_bytes == 259
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_context_manager(self, super_mock):
#         wrapped = MockFile(ZEN)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         mock.__exit__.side_effect = wrapped.__exit__
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             assert super_mock.init_called == 1
#             assert not mock.__enter__.called
#             file.read()
#         assert not mock.__enter__.called
#         mock.__exit__.assert_called_once_with(None, None, None)
#         assert len(mock.mock_calls) == 2
#         with pytest.raises(ValueError, match="I/O operation on closed file."):
#             file.read()
#         with pytest.raises(ValueError, match="I/O operation on closed file."):
#             file.write(b"data")
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_context_manager_exception_raise(self, super_mock):
#         exception = MockException("Should raise")
#         wrapped = MockFile(ZEN, exception=exception)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         mock.__exit__.side_effect = wrapped.__exit__
#         super_mock.mock_object = mock
#         with pytest.raises(MockException, match="Should raise") as err:
#             with MeteredFile() as file:
#                 assert not mock.__enter__.called
#                 file.read()
#         assert not mock.__enter__.called
#         mock.__exit__.assert_called_once_with(
#             MockException,
#             err.value,
#             ANY,
#         )
#         assert exception == err.value
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_context_manager_exception_suppress(self, super_mock):
#         exception = MockException("Should suppress")
#         wrapped = MockFile(ZEN, exception=exception)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         mock.__exit__.side_effect = wrapped.__exit__
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             assert not mock.__enter__.called
#             file.read()
#         assert not mock.__enter__.called
#         mock.__exit__.assert_called_once_with(
#             MockException,
#             exception,
#             ANY,
#         )
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_iteration(self, super_mock):
#         mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
#         super_mock.mock_object = mock
#         actual_reads = b""
#         file = MeteredFile()
#         for line in file:
#             actual_reads += line
#             assert mock.readline.call_count > 0, "File's readline not called"
#             assert mock.readline.call_count < 50, "Possible infinite loop detected"
#             assert file.read_ops == mock.readline.call_count
#         assert not mock.__iter__.called
#         assert file.read_bytes == len(ZEN)
#         assert actual_reads == ZEN
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_read_once(self, super_mock):
#         mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             actual_read = file.read()
#         assert actual_read == ZEN
#         assert file.read_bytes == len(ZEN)
#         assert file.read_ops == 1
#         assert mock.read.call_count == file.read_ops
#
#         mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             actual_read = file.read(None)
#         assert actual_read == ZEN
#         assert file.read_bytes == len(ZEN)
#         assert file.read_ops == 1
#         assert mock.read.call_count == file.read_ops
#
#         mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             actual_read = file.read(-1)
#         assert actual_read == ZEN
#         assert file.read_bytes == len(ZEN)
#         assert file.read_ops == 1
#         assert mock.read.call_count == file.read_ops
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_read_multiple(self, super_mock):
#         wrapped = MockFile(ZEN)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         super_mock.mock_object = mock
#         actual_read = b""
#         with MeteredFile() as file:
#             for _ in range(5):
#                 actual_read += file.read(30)
#         assert actual_read == ZEN[:150]
#         assert file.read_ops == 5
#         assert file.read_bytes == 150
#         assert mock.read.call_count == 5
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_read_multiple_chunk(self, super_mock):
#         wrapped = MockFile(ZEN, chunk=20)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         super_mock.mock_object = mock
#         actual_read = b""
#         with MeteredFile() as file:
#             for _ in range(5):
#                 actual_read += file.read()
#             actual_read += file.read(10)
#         assert actual_read == ZEN[:110]
#         assert file.read_ops == 6
#         assert file.read_bytes == 110
#         assert mock.read.call_count == 6
#
#         wrapped = MockFile(ZEN, chunk=20)
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         super_mock.mock_object = mock
#         actual_read = b""
#         with MeteredFile() as file:
#             for size in [None, -2, -1, 0, 1, 2]:
#                 actual_read += file.read(size)
#             actual_read += file.read(10)
#         assert actual_read == ZEN[:73]
#         assert file.read_ops == 7
#         assert file.read_bytes == 73
#         assert mock.read.call_count == 7
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_read_under_size(self, super_mock):
#         wrapped = MockFile(ZEN, chunk=257)  # largish odd number
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             actual_read = file.read()
#         assert actual_read == ZEN[:257]
#         assert file.read_ops == 1
#         assert file.read_bytes == 257
#         assert mock.read.call_count == 1
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_write_once(self, super_mock):
#         wrapped = MockFile(chunk=257)  # largish odd number
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             write_len = file.write(ZEN)
#             assert wrapped.getbuffer() == ZEN[:257]
#         assert write_len == 257
#         assert file.write_ops == 1
#         assert file.write_bytes == 257
#         assert mock.write.call_count == 1
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_write_multiple(self, super_mock):
#         wrapped = MockFile()
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         super_mock.mock_object = mock
#         write_len = 0
#         expected = b"Tomorrow's victory is today's practice."
#         with MeteredFile() as file:
#             write_len += file.write(b"Tomorro")
#             write_len += file.write(b"w's victo")
#             write_len += file.write(b"ry is today")
#             write_len += file.write(b"'s practice.")
#             assert wrapped.getbuffer() == expected
#         assert write_len == 39
#         assert file.write_ops == 4
#         assert file.write_bytes == 39
#         assert mock.write.call_count == 4
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_write_under_size(self, super_mock):
#         wrapped = MockFile(chunk=257)  # largish odd number
#         mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             write_len = file.write(ZEN[:123])
#             assert wrapped.getbuffer() == ZEN[:123]
#         assert write_len == 123
#         assert file.write_ops == 1
#         assert file.write_bytes == 123
#         assert mock.write.call_count == 1
#
#     @patch("paasio.super", create=True, new_callable=SuperMock)
#     def test_meteredfile_stats_read_only(self, super_mock):
#         mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
#         super_mock.mock_object = mock
#         with MeteredFile() as file:
#             assert file.read_ops == 0
#             assert file.read_bytes == 0
#             for _ in range(57):
#                 file.read(1)
#             file.read(2)
#             assert file.read_ops == 58
#             assert file.read_bytes == 59
#             assert file.write_ops == 0
#             assert file.write_bytes == 0
#             for _ in range(77):
#                 file.write(b"b")
#             file.write(b"bytes")
#             assert file.write_ops == 78
#             assert file.write_bytes == 82
#             with pytest.raises(
#                 AttributeError,
#                 match="property 'write_ops' of 'MeteredFile' object has no setter",
#             ):
#                 file.write_ops = 0
#             with pytest.raises(
#                 AttributeError,
#                 match="property 'write_bytes' of 'MeteredFile' object has no setter",
#             ):
#                 file.write_bytes = 0
#             with pytest.raises(
#                 AttributeError,
#                 match="property 'read_ops' of 'MeteredFile' object has no setter",
#             ):
#                 file.read_ops = 0
#             with pytest.raises(
#                 AttributeError,
#                 match="property 'read_bytes' of 'MeteredFile' object has no setter",
#             ):
#                 file.read_bytes = 0
#             assert file.write_ops == 78
#             assert file.write_bytes == 82
#             assert file.read_ops == 58
#             assert file.read_bytes == 59
#
