# Python_BehaveBDD
python + behave + allure_report

To Generate xml report :
behave --junit ./featurefile

To Generate json report :
behave -f allure_behave.formatter:AllureFormatter
 -o reports features/staticlogin.feature


