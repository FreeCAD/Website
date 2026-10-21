---
title: Guia do CLion
description: Guia para começar a usar o CLion.
weight: 5
---

Se você ainda não tem o CLion instalado, baixe-o, licencie-o e instale-o conforme as instruções da JetBrains.

### Obtendo o FreeCAD

**Linha de comando:**   `git clone --recurse-submodules https://github.com/freecad/freecad` e depois File -> Open ou New Project nesse diretório.

**IDE:** no canto superior esquerdo, escolha Project from Version Control.   Use https://github.com/freecad/freecad
![Pict8](CLionPythonDebug8.webp)

### Configurar a toolchain do Pixi (opcional)

Se você optar por usar o Pixi para obter as dependências, precisará configurar uma toolchain do CLion e atribuí-la ao seu perfil do CMake.

1. Execute `pixi shell` no diretório local do FreeCAD para obter todos os pacotes; isso também é necessário para atualizar o ambiente depois que o `pixi.toml` for alterado.
2. Vá em Settings &rarr; Build, Execution, Deployment &rarr; Toolchains.
3. Crie uma nova toolchain "System".
4. Clique em "Add environment" e selecione "From file".
5. Informe o local do script `pixi-default.bat` no Windows, ou do script `pixi-default.bash` nos demais sistemas, no campo "Environment file". O arquivo pode ser encontrado no repositório do FreeCAD em contrib/clion/pixi

![PixiPict1](CLionPixi1.webp)

6. Vá em Settings &rarr; Build, Execution, Deployment &rarr; CMake.
7. Selecione a predefinição "conda-[your os]-debug" ou "conda-[your os]-release" e duplique-a.
8. Ative o perfil duplicado e atribua a ele a toolchain criada.
9. No Windows, você também precisa selecionar o gerador do Visual Studio.

![PixiPict2](CLionPixi2.webp)

Observação: se o CMake não detectar nenhum pacote da pasta .pixi, o script da toolchain pode ter falhado.
Isso pode ser resolvido usando o caminho absoluto do seu repositório do FreeCAD no script `pixi-default.bash`.

### Compilando o CMake

O CLion deve atualizar automaticamente a compilação CMake do aplicativo.  Você vê os resultados ou executa novamente usando a seleção
cmake no canto inferior direito
![Pict9](CLionPythonDebug9.webp)

### Compilando o aplicativo

Escolha uma configuração ( Debug ) e um target ( FreeCADMain ) na barra superior.  First time through, use the menus to
run 'Build All in Debug' from the Build Menu.  After that point you can generally just Run or Debug and it will build
any dependencies for you.  Note that if you switch branches you may sometimes need to "Rebuild All in Debug" to force
a clean full rebuild.

![Pict10](CLionPythonDebug10.webp)
![Pict11](CLionPythonDebug11.webp)

### Running Application

Use the Run or Debug Icons from the top bar shown in the prior image.

## Debugging

While CLion supports both a C++ debugger and a Python debugger, it generally does not support
embedded Python interpreters, nor debugging both simultaneously.  However, there are workaround
procedures that will allow this.

### Basic C++ concept

CLion invokes an underlying debugger that launches or connects to the program under
test.  You can see this in the "Attach to Process" dialog under the Run menu.  After
choosing a process, you will be asked to attach with GDB or LLDB; CLion uses the
appropriate API to communicate with the debugger, which uses OS specific mechanisms
to control the program under test.

### Basic Python concept

The pydevd debugger is run inside of the python interpreter under test.  This provides
a network socket, normally connected _from_ the interpreter under test to a listening
socket in the controlling debugger UI.  This port defaults to 5678 for non-CLion uses.  CLion
generates a random port number, and then passes this into the pydevd initialization code;
if you run a python program then this is accomplished by directly running a shim with
parameters that include the port number and the program to be debugged.  In an attach
scenario, CLion _launches a C++ debugger_ to inject the pydevd initialization into the
running python interpreter and cause it to make the socket connection back to the UI.  Note
that since you generally cannot have more than one c++ debugger attached to a program,
this mechanism cannot work for a program already under c++ debugging, and since it assumes
that the c++ program is in fact a python process, it won't work for embedded python either.

### Technique for getting Python testing working

The challenge here is to get CLion to listen on a port for the incoming connection from pydevd,
and to execute pydevd on that port in the program under test.  Since CLion does not support this
natively, we trick it.  To do this we need to have a pydevd installed in the python interpreter in
FreeCAD.

### Running a basic c++ debug

Simply choose the debug option to start FreeCAD, and you're good to go.

### Setting up for python debugging in CLion

Use the settings button in the upper right, the File Menu -> Settings, or the Ctrl-Alt-S shortcut
to open the settings dialog, expand the Build, Execution, Deployment tree item, and select a Python
Interpreter:

![Pict1](CLionPythonDebug1.webp)

Install `pydevd` into the FreeCAD python environment, if it is not already present. For example:

```
C:\Users\jdoe\FreeCAD\cmake-build-relwithdebinfo-visual-studio\bin\python.exe -m pip install pydevd
```

Switch to the Python Debugger settings, and change the Attach To Process name from python to 'Freecad'
You may need to change this back if you use the IDE for other applications.

![Pict2](CLionPythonDebug2.webp)

Now there are three approaches here:

1. Using a recent version of CLion (at least 2024.3), ensure that the `python.debug.use.single.port` is checked in CLion's Registry (Help->Find action...->"Registry"), then in the Python Debugger settings page set the port to 5679. Note that this option will not appear if your registry setting is off (the default starting in 2024.3.1), so if you don't see the option to set the port, go back and double-check the registry setting.

2. Find the attach_pydevd.py file in your CLion installation, and modify it using the contrib/clion/attach_pydevd.py.patch in the source code.  Then use the macro below.

3. Use this elaborate workaround:

### Running a python or simultaneous debug using the non-intrusive procedure

1. You can start your FreeCAD independently, via CLion, or in c++ debug mode under CLion.

2. Regardless of the starting technique, once FreeCAD is up, if there is no code in your FreeCAD supporting
   CLion debugging, then:
   1. Go to the python console and import pydevd.
      Then go ahead and pretype in the settrace call, leaving the cursor poised to enter a port name but not executing the line.
   2. Alternatively, go to the Macro -> Attach to remote debugger dialog and switch to the CLion tab.

![Pict1](CLionPythonDebug6.webp)

3. Return to CLion, and start Attach to Process from the run menu:

![Pict1](CLionPythonDebug3.webp)

4. Find the Freecad process, which may be well down at the bottom of the list.  É a configuração
   feita anteriormente que faz os processos do Freecad aparecerem na lista como depuráveis em Python.  Destaque esta entrada
   e pressione o botão Attach with Python Debugger.

![Pict1](CLionPythonDebug4.webp)

5. Agora é hora de agir RÁPIDO.  Você tem cerca de 10 a 15 segundos para concluir o seguinte:
   Role até o topo da janela do console e encontre o número de porta (aleatório) em que o CLion escolheu
   escutar.  Ignore todo o resto:

![Pict1](CLionPythonDebug5.webp)

6. Mude para a janela do FreeCAD e complete o número da porta na linha settrace do console ou no diálogo de anexar
   e execute:

![Pict1](CLionPythonDebug6.webp)

7. Observe o aparecimento da linha "Connected to pydev debugger" no console do CLion.  Pouco antes ou depois dessa
   mensagem, você também verá o tempo esgotado da tentativa do CLion de usar um depurador para disparar a anexação.  Ignore este
   erro.

![Pict1](CLionPythonDebug7.webp)

8. Prossiga com a depuração normalmente:  quaisquer breakpoints existentes, no código C++ ou Python, serão atingidos; você
   pode avançar passo a passo, examinar variáveis, tudo.

### Executando uma depuração Python ou simultânea usando o CLion atualizado ou o attach_pydevd.py corrigido

1. Inicie a execução do FreeCAD.  Você pode fazer isso de qualquer lugar para apenas uma depuração Python; ou pode iniciar uma depuração C++
   no CLion para depuração simultânea.
2. Execute o contrib/clion/GetCLionDebugPort.FCMacro no FreeCAD.  A forma mais limpa de fazer isso é simplesmente adicioná-lo como
   primeiro parâmetro da linha de comando do FreeCAD ou do FreeCADCmd.  Editar a configuração de execução/depuração do FreeCADMain no
   CLion é a melhor forma de fazer isso: configure uma vez, e a depuração Python estará sempre disponível, quer você execute uma depuração C++
   ou não, sem perda de desempenho perceptível.

#### Advertências

- Às vezes você pode ter um breakpoint espúrio atingido no depurador Python.  Basta clicar no botão de continuar a execução para
  seguir em frente.  O FreeCAD dispara uma exceção Python durante a inicialização, e as configurações padrão do depurador do CLion fazem parar nessa
- condição.
- Os arquivos Python são copiados do código-fonte para o diretório de compilação.  Você deve usar essas versões dos arquivos Python
  no diretório de compilação se quiser definir breakpoints.  Então, se você compilou em `cmake-build-debug`, por exemplo, você
- vai querer `cmake-debug-build/Mod/BIM/Arch.py` e não `src/Mod/BIM/Arch.py`.  This also means that you need to be careful
  when editing files - anything in the build directory is essentially temporary and will be overwritten on the next build,
  but if you change something in the source directory then you need to run a build on an appropriate target to copy the
  changed python file to the build directory.  CLion does not support specifying mapping directories for this python code,
  and there is no evidence of it changing soon.
