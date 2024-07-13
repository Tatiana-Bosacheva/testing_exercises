import datetime
from decimal import Decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    sms = SmsMessage('2000 500, 5674 02.06.24 18:12 Lenta authcode 9999', 'anya', datetime.datetime(2024, 6, 2, 18, 12))
    cards = [BankCard('1522', 'tanya'), BankCard('5674', 'anya')]
    expense = Expense(amount=Decimal('2000'), card=BankCard(last_digits='5674', owner='anya'), spent_in='Lenta', spent_at=datetime.datetime(2024, 6, 2, 18, 12))
    assert parse_ineco_expense(sms, cards) ==  expense
