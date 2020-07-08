import unittest
from CardValidatorService import CardValidatorService as ServiceClass


class ServiceTests(unittest.TestCase):
    def test_one(self):
        solution_service = ServiceClass()
        result = solution_service.get_validation_result("50\n" + \
                                                    "1182387522195848\n" + \
                                                    "4898285859544556\n" + \
                                                    "3533946521218854\n" + \
                                                    "2178579985193175\n" + \
                                                    "9691928949545344\n" + \
                                                    "1327576477684519\n" + \
                                                    "6885867822596993\n" + \
                                                    "1958129523778579\n" + \
                                                    "2357676157819124\n" + \
                                                    "9832746248713726\n" + \
                                                        "3673159777236652\n" + \
                                                        "8626186974574971\n" + \
                                                        "9687622296992497\n" + \
                                                        "6731749895254584\n" + \
                                                        "8231635922318254\n" + \
                                                        "7728878259735616\n" + \
                                                        "3347275338764373\n" + \
                                                        "6624557432269847\n" + \
                                                        "3164653818478977\n" + \
                                                        "7683817293887423\n" + \
                                                        "4654491168789767\n" + \
                                                        "6942469919536219\n" + \
                                                        "8434524674271379\n" + \
                                                        "6619249165433473\n" + \
                                                        "8842787232483367\n" + \
                                                        "5349898497837349\n" + \
                                                        "4841565975496529\n" + \
                                                        "7635659522159832\n" + \
                                                        "6699889899699968\n" + \
                                                        "5274676861386577\n" + \
                                                        "7261479482325831\n" + \
                                                        "9855821811363989\n" + \
                                                        "5462941623272486\n" + \
                                                        "2168457338741692\n" + \
                                                        "3493828267535654\n" + \
                                                        "7688277563695358\n" + \
                                                        "4621162653647299\n" + \
                                                        "5588937472734175\n" + \
                                                        "6313634439334582\n" + \
                                                        "2621731928824298\n" + \
                                                        "9356326214767474\n" + \
                                                        "6399396262113367\n" + \
                                                        "7326622854597675\n" + \
                                                        "2179646384144599\n" + \
                                                        "8723731421194264\n" + \
                                                        "9893925198222769\n" + \
                                                        "8493394862176119\n" + \
                                                        "9182146786584817\n" + \
                                                        "7865278423923993\n" + \
                                                        "5437343432579992")
        self.assertEqual("Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Valid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid", result)

    def test_two(self):
        solution_service = ServiceClass()
        result = solution_service.get_validation_result("6\n" + \
                                                    "4123456789123456\n" + \
                                                    "5123-4567-8912-3456\n" + \
                                                    "61234-567-8912-3456\n" + \
                                                    "4123356789123456\n" + \
                                                    "5133-3367-8912-3456\n" + \
                                                    "5123 - 3567 - 8912 - 3456")
        self.assertEqual("Valid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Invalid", result)

    def test_three(self):
        solution_service = ServiceClass()
        result = solution_service.get_validation_result("6\n" + \
                                                    "3695-7963-915827-75\n" + \
                                                    "3143-4672-8798-2968-2968\n" + \
                                                    "6444-4444-4444-4918\n" + \
                                                    "6865396515642918\n" + \
                                                    "6865396515642\n" + \
                                                    "4695-7963-9778-2775")
        self.assertEqual("Invalid\n" + \
                         "Invalid\n" + \
                         "Invalid\n" + \
                         "Valid\n" + \
                         "Invalid\n" + \
                         "Valid", result)


if __name__ == '__main__':
    unittest.main()
