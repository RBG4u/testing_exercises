from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import pytest
import datetime
import decimal

@pytest.fixture
def cards():
    return [
            BankCard(last_digits='1234', owner='Tony'),
            BankCard(last_digits='5678', owner='Maylo')
            ]


#@pytest.fixture(name='cards')
##def fix_cards(cards):
#    print(cards)


def test_parse_ineco_expense(cards):
    sms = SmsMessage(
                       text='Spending 1500 RUB, VISA-1234 25.05.23 14:30 SHOP authcode 123456', 
                       author='BANK', 
                       sent_at=datetime.datetime.now()
                       )

    result = parse_ineco_expense(sms, cards)

    assert result.amount == decimal.Decimal('1500')
    assert result.card == cards[0]
    assert result.spent_in == 'SHOP'
    assert result.spent_at == datetime.datetime(2023, 5, 25, 14, 30)