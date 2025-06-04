### Hexlet tests and linter status:

[![Actions Status](https://github.com/IvanFoksha/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/IvanFoksha/python-project-50/actions)

[![Build](https://github.com/IvanFoksha/python-project-50/actions/workflows/python.yml/badge.svg)](https://github.com/IvanFoksha/python-project-50/actions/workflows/python.yml)

[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=IvanFoksha_python-project-50&metric=alert_status)](https://sonarcloud.io/dashboard?id=IvanFoksha_python-project-50)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=IvanFoksha_python-project-50&metric=coverage)](https://sonarcloud.io/dashboard?id=IvanFoksha_python-project-50)

### Пример использования

##### Сравниваем два конфигурационных файла в формате json:

```bash
gendiff tests/fixtures/file1.json tests/fixtures/file2.json
# Вывод:
# {
#   - follow: False
#     host: hexlet.io
#   - proxy: 123.234.53.22
#   - timeout: 50
#   + timeout: 20
#   + verbose: True
# }
```

Полная демонстрация в терминале:

[![asciicast](https://asciinema.org/a/LEhB5qnHrrsjQmYQ0qIM8E2p4.svg)](https://asciinema.org/a/LEhB5qnHrrsjQmYQ0qIM8E2p4)

##### Сравниваем два конфигурационных файла в формате yml и yaml:

```bash
gendiff tests/fixtures/file1.yml tests/fixtures/file2.yaml
# Вывод:
# {
#   - follow: false
#     host: hexlet.io
#   - proxy: 123.234.53.22
#   - timeout: 50
#   + timeout: 20
#   + verbose: true
# }
```

Полная демострация в терминале:

[![asciicast](https://asciinema.org/a/tXqvjbQbSmj2uEdttTR4Lbhpb.svg)](https://asciinema.org/a/tXqvjbQbSmj2uEdttTR4Lbhpb)

##### Сравниваем два конфигурационных файла с помощью рекурсивного сравнения

```bash
uv run gendiff tests/test_data/file1.json tests/test_data/file2.json
# Вывод:
# {
#   common: {
#     + follow: false
#       setting1: Value 1
#     - setting2: 200
#     - setting3: true
#     + setting3: null
#     + setting4: blah blah
#     + setting5: {
#           key5: value5
#       }
#       setting6: {
#         - wow:
#         + wow: so much
#           key: value
#         + ops: vops
#       }
#   }
#   group1: {
#     - baz: bas
#     + baz: bars
#       foo: bar
#     - nest: {
#           key: value
#       }
#     + nest: str
#   }
# - group2: {
#       abc: 12345
#       deep: {
#           id: 45
#       }
#   }
# + group3: {
#       deep: {
#           id: {
#               number: 45
#           }
#       }
#       fee: 100500
#   }
# }
```

Полная демонстрация в терминале:

[![asciicast](https://asciinema.org/a/b3dVFWyOo6SMffXrjAPc61B7T.svg)](https://asciinema.org/a/b3dVFWyOo6SMffXrjAPc61B7T)
