# Python

- [Python](#python)
  - [Sonarqube](#sonarqube)

## Sonarqube

> Unfortunately Mariadb isn't support so Sonarqube will use PostgreSQL.

1. Create the directory where Sonarqube's certificates will be stored:

```shell
mkdir -p ${HOME}/.sonarqube/certs
```

2. Generate the needed keys:

```shell
keytool \
  -noprompt \
  -import \
  -storetype PKCS12 \
  -alias sonar \
  -keystore "${HOME}/.sonarqube/certs/truststore.p12" \
  -file "${HOME}/.certs/local-cert.pem" \
  -storepass "weekly"
```

3. Check if the keys were successful generated:

```shell
openssl pkcs12 \
  -in "${HOME}/.sonarqube/certs/truststore.p12" \
  -passin pass:"weekly" \
  -info \
  -nokeys
```

4. Run the analysis but remember first to change `PROJECT_NAME_HERE` and `PROJECT_GENERATED_KEY_HERE` before running it:

```shell
docker run \
  --rm \
  --network=host \
  --workdir "/usr/src/" \
  --volume "${HOME}/.sonarqube/certs/:/opt/sonar-scanner/.sonar/ssl/:ro" \
  --volume "${PWD}:/usr/src" \
  sonarsource/sonar-scanner-cli:11.3 \
  -X \
  -Dsonar.projectKey=PROJECT_NAME_HERE \
  -Dsonar.scanner.truststorePassword="weekly" \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonarqube.docker.localhost/ \
  -Dsonar.login=PROJECT_GENERATED_KEY_HERE
```
