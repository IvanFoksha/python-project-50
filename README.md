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

##### Сравниваем два конфигурационных файла в плоском формате:

```bash
uv run gendiff tests/test_data/file1.json tests/test_data/file2.json -f plain
# Вывод:
# Property 'common.follow' was added with value: false
# Property 'common.setting2' was removed
# Property 'common.setting3' was updated. From true to null
# Property 'common.setting4' was added with value: 'blah blah'
# Property 'common.setting5' was added with value: [complex value]
# Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
# Property 'common.setting6.ops' was added with value: 'vops'
# Property 'group1.baz' was updated. From 'bas' to 'bars'
# Property 'group1.nest' was updated. From [complex value] to 'str'
# Property 'group2' was removed
# Property 'group3' was added with value: [complex value]
```

Полная демострация в терминале:

[![asciicast](https://asciinema.org/a/dxS2k6JHA94CkcY1tt7BVNEoP.svg)](https://asciinema.org/a/dxS2k6JHA94CkcY1tt7BVNEoP)

##### Сравниваем два конфигурационных файла с выводом в JSON:

```bash
uv run gendiff tests/test_data/file1.json tests/test_data/file2.json -f json
# Вывод:
# [
#   {
#     "type": "nested",
#     "key": "common",
#     "children": [
#       {
#         "type": "added",
#         "key": "follow",
#         "value": false
#       },
#       {
#         "type": "unchanged",
#         "key": "setting1",
#         "value": "Value 1"
#       },
#       {
#         "type": "removed",
#         "key": "setting2",
#         "value": 200
#       },
#       {
#         "type": "changed",
#         "key": "setting3",
#         "old_value": true,
#         "new_value": null
#       },
#       {
#         "type": "added",
#         "key": "setting4",
#         "value": "blah blah"
#       },
#       {
#         "type": "added",
#         "key": "setting5",
#         "value": {
#           "key5": "value5"
#         }
#       },
#       {
#         "type": "nested",
#         "key": "setting6",
#         "children": [
#           {
#             "type": "nested",
#             "key": "doge",
#             "children": [
#               {
#                 "type": "changed",
#                 "key": "wow",
#                 "old_value": "",
#                 "new_value": "so much"
#               }
#             ]
#           },
#           {
#             "type": "unchanged",
#             "key": "key",
#             "value": "value"
#           },
#           {
#             "type": "added",
#             "key": "ops",
#             "value": "vops"
#           }
#         ]
#       }
#     ]
#   },
#   {
#     "type": "nested",
#     "key": "group1",
#     "children": [
#       {
#         "type": "changed",
#         "key": "baz",
#         "old_value": "bas",
#         "new_value": "bars"
#       },
#       {
#         "type": "unchanged",
#         "key": "foo",
#         "value": "bar"
#       },
#       {
#         "type": "changed",
#         "key": "nest",
#         "old_value": {
#           "key": "value"
#         },
#         "new_value": "str"
#       }
#     ]
#   },
#   {
#     "type": "removed",
#     "key": "group2",
#     "value": {
#       "abc": 12345,
#       "deep": {
#         "id": 45
#       }
#     }
#   },
#   {
#     "type": "added",
#     "key": "group3",
#     "value": {
#       "deep": {
#         "id": {
#           "number": 45
#         }
#       },
#       "fee": 100500
#     }
#   }
# ]
```

Полная демострация в терминале:

[![asciicast](https://asciinema.org/a/8LeJ5lrukxEMYOuzaajExa43Q.svg)](https://asciinema.org/a/8LeJ5lrukxEMYOuzaajExa43Q)
