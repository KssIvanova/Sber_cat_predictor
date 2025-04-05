# Ответы на вопросы по сетевому оборудованию

## 1. Параметры порта коммутатора

### Основные параметры:
- Скорость передачи данных (Speed)
- Дуплексный режим (Duplex)
- Состояние порта (Status)
- VLAN
- Настройки безопасности
- QoS (Quality of Service)

### Примеры команд для настройки:
```cisco
! Настройка скорости и дуплекса
Switch(config-if)# speed 1000
Switch(config-if)# duplex full

! Настройка VLAN
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10

! Настройка QoS
Switch(config-if)# mls qos trust cos
```

## 2. Средства блокировки несанкционированных подключений

### Основные методы:
1. Port Security
2. MAC-адрес фильтрация
3. 802.1X аутентификация
4. VLAN изоляция
5. ACL (списки контроля доступа)

### Примеры команд:
```cisco
! Настройка Port Security
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 2
Switch(config-if)# switchport port-security violation restrict

! Настройка 802.1X
Switch(config-if)# dot1x port-control auto
Switch(config-if)# dot1x pae authenticator

! Настройка ACL
Switch(config)# ip access-list extended BLOCK_UNAUTHORIZED
Switch(config-ext-nacl)# deny ip any any
Switch(config-if)# ip access-group BLOCK_UNAUTHORIZED in
```

## 3. Параметры команды switchport port-security

### Основные параметры:
1. maximum [1-132] - максимальное количество MAC-адресов
2. violation {protect | restrict | shutdown} - действие при нарушении
3. mac-address [MAC-ADDRESS] - статическое назначение MAC-адреса
4. aging {static | time [0-1440]} - настройка времени старения

### Примеры команд:
```cisco
! Настройка максимального количества MAC-адресов
Switch(config-if)# switchport port-security maximum 3

! Настройка действий при нарушении
Switch(config-if)# switchport port-security violation shutdown

! Настройка статического MAC-адреса
Switch(config-if)# switchport port-security mac-address 0001.0001.0001

! Настройка времени старения
Switch(config-if)# switchport port-security aging time 60
```

## 4. Привязка MAC-адреса

### Преимущества:
- Ограничение доступа по MAC-адресам
- Повышение безопасности сети
- Предотвращение несанкционированных подключений
- Отслеживание подключений устройств

### Примеры команд:
```cisco
! Настройка статического MAC-адреса
Switch(config-if)# switchport port-security mac-address 0001.0001.0001

! Настройка sticky MAC-адресов
Switch(config-if)# switchport port-security mac-address sticky

! Просмотр настроенных MAC-адресов
Switch# show port-security address
```

## 5. Просмотр адреса "нарушителя"

### Команды для просмотра:
```cisco
! Просмотр информации о безопасности порта
Switch# show port-security interface fastEthernet 1/0/1

! Просмотр всех нарушений
Switch# show port-security violations

! Просмотр подробной информации
Switch# show port-security address
```

## 6. Счетчик нарушений

### Увеличивается при:
- Подключении устройства с неразрешенным MAC-адресом
- Превышении лимита MAC-адресов
- Нарушении настроек безопасности порта

### Примеры команд:
```cisco
! Просмотр счетчиков нарушений
Switch# show port-security interface fastEthernet 1/0/1

! Сброс счетчиков
Switch# clear port-security counters
```

## 7. Действия при отключении "нарушителя"

### Процесс:
1. Сброс счетчика нарушений
2. Возврат порта в рабочее состояние
3. Возобновление нормальной работы

### Команды:
```cisco
! Включение порта после нарушения
Switch(config-if)# no shutdown

! Сброс состояния безопасности
Switch# clear port-security
```

## 8. CDP (Cisco Discovery Protocol)

### Основные характеристики:
- Протокол канального уровня
- Работает только между устройствами Cisco
- Отправляет информацию каждые 60 секунд
- Holdtime: 180 секунд

### Команды:
```cisco
! Включение/выключение CDP
Switch(config)# cdp run
Switch(config)# no cdp run

! Настройка CDP на интерфейсе
Switch(config-if)# cdp enable
Switch(config-if)# no cdp enable

! Просмотр информации CDP
Switch# show cdp neighbors
Switch# show cdp neighbors detail
```

## 9. ARP (Address Resolution Protocol)

### Основные характеристики:
- Протокол сетевого уровня
- Преобразует IP в MAC-адреса
- Кэширует результаты в ARP-таблице

### Команды:
```cisco
! Просмотр ARP-таблицы
Switch# show ip arp

! Очистка ARP-кэша
Switch# clear arp-cache

! Настройка статических ARP-записей
Switch(config)# arp 192.168.1.1 0001.0001.0001 arpa
```

## 10. Информация через CDP

### Получаемая информация:
- Имя устройства
- Тип устройства
- Версия ПО
- IP-адреса
- Интерфейсы
- Возможности устройства

### Команды:
```cisco
! Просмотр общей информации
Switch# show cdp

! Просмотр детальной информации
Switch# show cdp neighbors detail

! Просмотр информации о конкретном интерфейсе
Switch# show cdp interface fastEthernet 1/0/1
```

## 11. Изменение CAM-таблицы

### Случаи изменения:
- При получении новых MAC-адресов
- При истечении времени старения
- При изменении топологии
- При перезагрузке

### Команды:
```cisco
! Просмотр CAM-таблицы
Switch# show mac address-table

! Очистка CAM-таблицы
Switch# clear mac address-table

! Настройка времени старения
Switch(config)# mac address-table aging-time 300
```

## 12. Изменение ARP-таблицы коммутатора

### Случаи изменения:
- При получении ARP-запросов
- При истечении времени жизни
- При изменении IP-адресов

### Команды:
```cisco
! Просмотр ARP-таблицы
Switch# show ip arp

! Настройка времени жизни ARP-записей
Switch(config)# arp timeout 300

! Очистка ARP-кэша
Switch# clear arp-cache
```

## 13. Изменение ARP-таблицы узла

### Случаи изменения:
- При отправке пакетов
- При получении ARP-ответов
- При истечении времени жизни
- При изменении сетевой конфигурации

### Команды для Windows:
```cmd
! Просмотр ARP-таблицы
arp -a

! Очистка ARP-кэша
arp -d

! Добавление статической записи
arp -s 192.168.1.1 00-11-22-33-44-55
```

### Команды для Linux:
```bash
! Просмотр ARP-таблицы
arp -n

! Очистка ARP-кэша
arp -d

! Добавление статической записи
arp -s 192.168.1.1 00:11:22:33:44:55
``` 