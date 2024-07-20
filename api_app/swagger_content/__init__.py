from drf_spectacular.utils import extend_schema, extend_schema_view


house = extend_schema_view(
    list=extend_schema(
        summary='Список домов',
        tags=['House']
    ),
    retrieve=extend_schema(
        summary='Просмотр дома',
        tags=['House']
    ),
    create=extend_schema(
        summary='Создать дом',
        tags=['House']
    ),
    update=extend_schema(
        summary='Редактировать дом',
        tags=['House']
    ),
    partial_update=extend_schema(
        summary='Редактировать дом',
        tags=['House']
    ),
    destroy=extend_schema(
        summary='Удаление дома',
        tags=['House']
    )
)


apartment = extend_schema_view(
    list=extend_schema(
        summary='Список квартир',
        tags=['Apartment']
    ),
    retrieve=extend_schema(
        summary='Просмотр квартиры',
        tags=['Apartment']
    ),
    create=extend_schema(
        summary='Создать квартиру',
        tags=['Apartment']
    ),
    update=extend_schema(
        summary='Редактировать квартиру',
        tags=['Apartment']
    ),
    partial_update=extend_schema(
        summary='Редактировать квартиру',
        tags=['Apartment']
    ),
    destroy=extend_schema(
        summary='Удаление квартиры',
        tags=['Apartment']
    )
)


tariff = extend_schema_view(
    list=extend_schema(
        summary='Список тарифов',
        tags=['Tariff']
    ),
    retrieve=extend_schema(
        summary='Просмотр тарифа',
        tags=['Tariff']
    ),
    create=extend_schema(
        summary='Создать тариф',
        tags=['Tariff']
    ),
    update=extend_schema(
        summary='Редактировать тариф',
        tags=['Tariff']
    ),
    partial_update=extend_schema(
        summary='Редактировать тариф',
        tags=['Tariff']
    ),
    destroy=extend_schema(
        summary='Удаление тарифа',
        tags=['Tariff']
    )
)

water_meter = extend_schema_view(
    list=extend_schema(
        summary='Список счётчиков',
        tags=['Water meter']
    ),
    retrieve=extend_schema(
        summary='Просмотр счётчика',
        tags=['Water meter']
    ),
    create=extend_schema(
        summary='Создать счётчик',
        tags=['Water meter']
    ),
    update=extend_schema(
        summary='Редактировать счётчик',
        tags=['Water meter']
    ),
    partial_update=extend_schema(
        summary='Редактировать счётчик',
        tags=['Water meter']
    ),
    destroy=extend_schema(
        summary='Удаление счётчика',
        tags=['Water meter']
    )
)

water_meter_reading = extend_schema_view(
    list=extend_schema(
        summary='Список показателей счётчиков',
        tags=['Water meter reading']
    ),
    retrieve=extend_schema(
        summary='Просмотр показателей счётчика',
        tags=['Water meter reading']
    ),
    create=extend_schema(
        summary='Добавить показатели счётчика',
        tags=['Water meter reading']
    ),
    update=extend_schema(
        summary='Редактировать показатели счётчика',
        tags=['Water meter reading']
    ),
    partial_update=extend_schema(
        summary='Редактировать показатели счётчика',
        tags=['Water meter reading']
    ),
    destroy=extend_schema(
        summary='Удаление показателя счётчика',
        tags=['Water meter reading']
    )
)


calculate_payment_in_house = extend_schema_view(
    post=extend_schema(
        summary='Расчёт квартплаты для всех квартир в доме за определёнынй месяц',
        tags=['Calculate payment']
    ),
    get=extend_schema(
        summary='Получить прогресс расчёта',
        tags=['Calculate payment']
    )
)