from typing import Dict, List, TypedDict


class Parsed(TypedDict):
    properties: Dict[str, List[str]]
    children: List["Parsed"]


class SGF:
    def __init__(self) -> None:
        self.__parsed__: Parsed = {
            "properties": {},
            "children": [],
        }

    def __repr__(self) -> str:
        return f"SGF({self.__parsed__})"

    def __parse_property_value(self, value: str) -> str:
        result = []
        i = 0
        while i < len(value):
            if value[i] == "\\":
                if i + 1 < len(value):
                    next_char = value[i + 1]
                    if next_char == "\n":
                        i += 1  # Skip newline after backslash
                    else:
                        result.append(next_char)
                        i += 1
                else:
                    result.append("\\")
            else:
                if value[i] == "\n":
                    result.append("\n")
                elif value[i].isspace():
                    result.append(" ")
                else:
                    result.append(value[i])
            i += 1
        return "".join(result)

    def __parse_properties(self, data: str) -> Dict[str, List[str]]:
        if not data:
            return {}

        properties: Dict[str, List[str]] = {}
        current_key = []
        current_value = []
        state = "key"
        escaped = False

        i = 0
        while i < len(data):
            char = data[i]

            if state == "key":
                if char == "[" and not escaped:
                    if not current_key:
                        raise ValueError("property without key")
                    key = "".join(current_key)
                    if not key.isupper():
                        raise ValueError("property must be in uppercase")
                    properties[key] = []
                    current_key = []
                    state = "value"
                    current_value = []
                else:
                    if char == "\\" and not escaped:
                        escaped = True
                    else:
                        current_key.append(char)
                        escaped = False

            elif state == "value":
                if char == "\\" and not escaped:
                    escaped = True
                    current_value.append(char)
                elif escaped:
                    escaped = False
                    current_value.append(char)
                elif char == "]" and not escaped:
                    processed_value = self.__parse_property_value(
                        "".join(current_value)
                    )
                    properties[key].append(processed_value)
                    current_value = []
                    state = "between"
                else:
                    current_value.append(char)

            elif state == "between":
                if char == "[" and not escaped:
                    state = "value"
                    current_value = []
                else:
                    if char == "\\" and not escaped:
                        escaped = True
                    else:
                        current_key.append(char)
                        escaped = False
                    state = "key"

            i += 1

        if state == "value" and current_value:
            raise ValueError("unterminated property value")
        if state == "key" and current_key:
            raise ValueError("property without delimiter")

        if not properties:
            raise ValueError("properties without delimiter")

        return properties

    def parse(self, sequence: str) -> Parsed:
        if not sequence or not sequence.startswith("(") or not sequence.endswith(")"):
            raise ValueError("tree missing")

        # Strip the outer parentheses, work on the core content
        content = sequence[1:-1]
        if not content:
            raise ValueError("tree with no nodes")

        # 1. Find the split between the root node and its variations
        in_prop = False
        escaped = False
        split_index = len(content)  # by default, all content is the root node
        for idx, ch in enumerate(content):
            if ch == "\\" and not escaped:
                escaped = True
                continue
            if escaped:
                escaped = False
                continue
            if ch == "[":
                in_prop = True
            elif ch == "]":
                in_prop = False
            # top-level '(' marks start of first variation
            elif ch == "(" and not in_prop:
                split_index = idx
                break

        root_node = content[:split_index]
        rest = content[split_index:]

        # 2. Parse root properties
        if not root_node.startswith(";"):
            props_str = root_node
        else:
            props_str = root_node[1:]
        self.__parsed__["properties"] = self.__parse_properties(props_str)

        # 3. Extract and recurse on each child variation
        children = []
        i = 0
        while i < len(rest):
            if rest[i] != "(":
                i += 1
                continue
            # match parentheses at top-level
            depth = 0
            in_prop = False
            escaped = False
            for j in range(i, len(rest)):
                c = rest[j]
                if c == "\\" and not escaped:
                    escaped = True
                    continue
                if escaped:
                    escaped = False
                    continue
                if c == "[":
                    in_prop = True
                elif c == "]":
                    in_prop = False
                elif c == "(" and not in_prop:
                    depth += 1
                elif c == ")" and not in_prop:
                    depth -= 1
                    if depth == 0:
                        # found the matching ')'
                        subtree = rest[i : j + 1]
                        child_parser = SGF()
                        child_parsed = child_parser.parse(subtree)
                        children.append(child_parsed)
                        i = j + 1
                        break
            else:
                raise ValueError("unmatched parenthesis in children")
        self.__parsed__["children"] = children

        return self.__parsed__


print(SGF().parse("(;A[B](;B[C])(;C[D]))"))
