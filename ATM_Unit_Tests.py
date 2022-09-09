from unittest import mock
from unittest import TestCase

import ATM

class ATMUnitTests(TestCase):
    @mock.patch('ATM.input', create=True)
    def testCalledRunATMMethodWrongPinAttemptThreetimes(self, mocked_input):
        expectedMessage = ['You have only 2 attempt left.', 'You have only 1 attempt left.', 'You have only 0 attempt left.']
        ATM.pinTotalattempt = 0
        ATM.allowedPinAttempt = 3
        mocked_input.side_effect = ['4521', '1547', '2456']
        actualmessage = ATM.RunAtm()
        self.assertEqual(actualmessage, expectedMessage)

    @mock.patch('ATM.input', create=True)
    def testCalledWithdrawCashEnteredAmountToWithdrawReceivedCash(self, mocked_input):
        expectedMessage = 90
        mocked_input.side_effect = ['10']
        actualmessage = ATM.Widthdraw_Cash(100)
        self.assertEqual(actualmessage, expectedMessage)

    @mock.patch('ATM.input', create=True)
    def testAtmWithdrawException(self, mocked_input):
        mocked_input.side_effect = ['110']
        self.assertRaises(Exception, ATM.Widthdraw_Cash, 100)

    @mock.patch('ATM.input', create=True)
    def testAtmWithdrawFormatException(self, mocked_input):
        mocked_input.side_effect = [26]
        self.assertRaises(Exception, ATM.Widthdraw_Cash, 100)

    @mock.patch('ATM.input', create=True)
    def testCalledValidatePin_EnteredAmountToWithdraw_ReceivedCash(self, mocked_input):
        expectedBalance = 80
        ATM.pinTotalattempt = 0
        ATM.allowedPinAttempt = 3
        mocked_input.side_effect = ['20']
        actuaalBalance = ATM.ValidatePin('1234','1234',100)
        self.assertEqual(expectedBalance, actuaalBalance)