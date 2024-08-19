from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'user': 'Ф.И.О:',
            'phone_number': 'Номер телефона',
            'sender_address': 'Адрес отправителя',
            'data_load': 'Дата загрузки груза',
            'destination': 'Место доставки груза (пункт назначения)',
            'cargo_type': 'Вид груза, его классификационное описание',
            'code': 'Товарный код',
            'marking': 'Маркировка',
            'country_origin': 'Страна происхождения',
            'cost': 'Стоимость  груза',
            'size': 'Размер упаковки',
            'volume': 'Объем',
            'number_seats': 'Количество мест',
            'weight': 'Вес /брутто, нетто/ всех мест',
            'transport_type': 'Вид транспорта и условия по отправке',
            'product_insurance': 'Указания о страховании груза (Осуществляется за счет Клиента)',
            'special_notes': 'Особые отметки',
            'tg_nickname': 'Никнейм в Telegram',
            'comment': 'Комментарий',
        }


fields_name = {
    'user': 'Ф.И.О',
    'phone_number': 'Номер телефона',
    'sender_address': 'Адрес отправителя',
    'data_load': 'Дата загрузки груза',
    'destination': 'Место доставки груза (пункт назначения)',
    'cargo_type': 'Вид груза, его классификационное описание',
    'code': 'Товарный код',
    'marking': 'Маркировка',
    'country_origin': 'Страна происхождения',
    'cost': 'Стоимость  груза',
    'size': 'Размер упаковки',
    'volume': 'Объем',
    'number_seats': 'Количество мест',
    'weight': 'Вес /брутто, нетто/ всех мест',
    'transport_type': 'Вид транспорта и условия по отправке',
    'product_insurance': 'Указания о страховании груза (Осуществляется за счет Клиента)',
    'special_notes': 'Особые отметки',
    'tg_nickname': 'Никнейм в Telegram',
    'comment': 'Комментарий',
}
