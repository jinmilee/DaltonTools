pwd
cd res/ui
pwd
echo "projeto_piloto.ui..."
pyuic4 projeto_piloto.ui > ../../lib/projeto_piloto.py
echo "mainWindowsCorrecao.ui..."
pyuic4 mainWindowCorrecao.ui > ../../lib/mainWindowsCorrecao.py
echo "visualizadorCorrecao.ui..."
pyuic4 visualizadorCorrecao.ui > ../../lib/visualizadorCorrecao.py
echo "pbar.ui..."
pyuic4 pbar.ui > ../../lib/pbar.py
echo "mainWindowSimulacao.ui"
pyuic4 mainWindowSimulacao.ui > ../../lib/mainWindowSimulacao.py
echo "visualizadorSimulacao.ui"
pyuic4 visualizadorSimulacao.ui > ../../lib/visualizadorSimulacao.py
cd -

