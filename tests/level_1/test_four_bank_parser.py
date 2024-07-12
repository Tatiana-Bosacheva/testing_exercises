import datetime
import pytest
from decimal import Decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense

@pytest.mark.parametrize(
        "sms, cards, expense", 
        [
            (SmsMessage('2000 500, 5674 02.06.24 18:12 Lenta authcode 9999', 'anya', datetime.datetime(2024, 6, 2, 18, 12)), [BankCard('1522', 'tanya'), BankCard('5674', 'anya')], Expense(amount=Decimal('2000'), card=BankCard(last_digits='5674', owner='anya'), spent_in='Lenta', spent_at=datetime.datetime(2024, 6, 2, 18, 12))),
            (SmsMessage('2000 500, 1522 02.06.24 18:12 Lenta authcode 9999', 'tanya', datetime.datetime(2024, 6, 2, 18, 12)), [BankCard('1522', 'tanya'), BankCard('5674', 'anya')], Expense(amount=Decimal('2000'), card=BankCard(last_digits='1522', owner='tanya'), spent_in='Lenta', spent_at=datetime.datetime(2024, 6, 2, 18, 12))),
        ]
)
def test_parse_ineco_expense(sms, cards, expense):
    assert parse_ineco_expense(sms, cards) ==  expense
