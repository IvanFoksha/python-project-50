### Hexlet tests and linter status:

[![Actions Status](https://github.com/IvanFoksha/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/IvanFoksha/python-project-50/actions)

[![Build](https://github.com/IvanFoksha/python-project-50/actions/workflows/python.yml/badge.svg)](https://github.com/IvanFoksha/python-project-50/actions/workflows/python.yml)

[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=IvanFoksha_python-project-50&metric=alert_status)](https://sonarcloud.io/dashboard?id=IvanFoksha_python-project-50)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=IvanFoksha_python-project-50&metric=coverage)](https://sonarcloud.io/dashboard?id=IvanFoksha_python-project-50)

### Пример использования

Сравниваем два конфигурационных файла:

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
