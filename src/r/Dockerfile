FROM r-base:4.4.3
LABEL author="fazenda"
LABEL project="weekly-exercises-r"

WORKDIR /usr/src/

RUN [ "apt", "update" ]
RUN [ "apt", "install", "--yes", "--allow-downgrades", \
  "git", \
  "pandoc", \
  "libexpat1=2.7.1-1", \
  "libexpat1-dev", \
  "libcurl4-openssl-dev", \
  "libgmp3-dev", \
  "libxml2-dev", \
  "libfreetype6-dev", \
  "libfribidi-dev", \
  "libharfbuzz-dev", \
  "libtiff-dev", \
  "libx11-dev", \
  "libgit2-dev", \
  "libfontconfig1-dev" \
]

RUN [ "R", "-e", "install.packages(c('renv', 'pak'), repos = 'https://cloud.r-project.org/')" ]

ENV RENV_CONFIG_PAK_ENABLED=TRUE
ENV RENV_CONFIG_PPM_URL='https://cloud.r-project.org/'

COPY renv.lock .

RUN [ "R", "-e", "renv::restore(prompt = FALSE)" ]

COPY .Rbuildignore .
COPY .lintr .
COPY NAMESPACE .
COPY DESCRIPTION .

COPY inst/ inst/
COPY docs/ docs/
COPY man/ man/
COPY tests/ tests/
COPY src/ src/
COPY R/ R/

RUN [ "R", "-e", "devtools::document()" ]
RUN [ "R", "-e", "renv::install('.')" ]
