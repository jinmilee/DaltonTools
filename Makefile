
PYUIC=pyuic4

default:
	echo "Use make uic/clean"


clean:
	for i in `find . -iname "*.pyc"`; do echo $$i ; rm $$i; done;
	for i in `ls lib/gui_*py 2> /dev/null`; do echo $$i; rm $$i; done;


uic:
	$(PYUIC) res/ui/gui_test_application.ui > lib/gui_test_application.py
	$(PYUIC) res/ui/gui_visualizator_window_simulator_application.ui > lib/gui_visualizator_window_simulator_application.py
	$(PYUIC) res/ui/gui_main_window_simulator_application.ui > lib/gui_main_window_simulator_application.py
	$(PYUIC) res/ui/gui_progress_bar.ui > lib/gui_progress_bar.py
	$(PYUIC) res/ui/gui_correct_application_main_window.ui > lib/gui_correct_application_main_window.py
	$(PYUIC) res/ui/gui_visualizator_window_correct_application.ui > lib/gui_visualizator_window_correct_application.py

