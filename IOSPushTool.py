#!/usr/bin/python# -*- coding: utf-8 -*# Filename: push.pyfrom pyapns import configure, provision, notifyimport osimport time#要先打开web服务器才能发推送消息#os.system("twistd -r kqueue web --class=pyapns.server.APNSServer --port=7077")#查看进程是否存在class IOSPushTool():    def __init__(self):        self.iphoneToken = '45bc04a779cd90b84255782a91c11523190ec3446f9e5b3eac059ae99f2b1e7d'        self.ipadToken = ''        self.webToken = ''        self.iMacToken = ''        self.configure = {'HOST': 'http://localhost:7077/'}        self.appid = 'com.woodcol.pushtest'        self.pemFile = 'ck.pem'        self.isSandbox = True        self.iostokens = ['45bc04a779cd90b84255782a91c11523190ec3446f9e5b3eac059ae99f2b1e7d']        self.pushCount = 0        self.notifications = [                              {'aps' :{'alert': 'Hello token 1', 'badge': 0, 'sound': 'flynn.caf'}}                              ]        self.runTwistd()    def runTwistd(self):        if self._isTwistdRun():            print "twistd is runed."        else:            print "start run twistd..."            os.system("twistd -r kqueue web --class=pyapns.server.APNSServer --port=7077")            print "start run ok"            def _isTwistdRun(self):        strtmp = os.popen("ps axu|grep twistd")         print type(strtmp)        cmdback = strtmp.read()        p = str(cmdback).find('--class=pyapns.server.APNSServer')        print p        if not p == -1:            print 'twistd is run:\n%s'%(str(cmdback))            return True        else:            print 'twistd is not run'            return False    def sendPushMsg(self,msg,deviceType = 'iphone'):        return        self.notifications = []        loctim = time.localtime()        #time.struct_time(tm_year=2015, tm_mon=8, tm_mday=2, tm_hour=12, tm_min=16, tm_sec=47, tm_wday=6, tm_yday=214, tm_isdst=0)        sendmsg = str(msg) + '|' + str(loctim.tm_hour) + ':' + str(loctim.tm_min) + ':' + str(loctim.tm_sec)        tmpnot = {'aps' :{'alert': sendmsg, 'badge': 0, 'sound': 'flynn.caf'}}        self.notifications.append(tmpnot)        configure(self.configure)        if self.isSandbox:            provision(self.appid, open(self.pemFile).read(),'sandbox')        else:            provision(self.appid, open(self.pemFile).read())        notify('com.woodcol.pushtest', self.iostokens, self.notifications)