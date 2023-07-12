@echo off

REM Command to execute unit tests
set unit_test_command=python -m unittest discover -s tests

REM Commands to run static analysis
set static_analysis_command=pylint .\src
set flake8_command=flake8 .\src

REM Execute unit tests
echo Running unit tests...
%unit_test_command%
set unit_test_exit_code=%errorlevel%

REM Perform static analysis
echo Static analysis...
echo pylint..
%static_analysis_command%
echo flake8..
%flake8_command%
