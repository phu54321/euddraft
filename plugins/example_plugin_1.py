from eudplib import *


def onPluginStart():
    DoActions(DisplayText('onPluginStart called'))


def beforeTriggerExec():
    DoActions(DisplayText('beforeTriggerExec called'))


def afterTriggerExec():
    DoActions(DisplayText('afterTriggerExec called'))
