#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Hello World

Make Cozmo say 'Hello World' in this simple Cozmo SDK example program.
'''
import cozmo
import speech_recognition as sr
import calendarday

def cozmo_program(robot: cozmo.robot.Robot):
    while True:
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source)

        try:
            from os import system
            print("You said " + r.recognize_google(audio))
            if r.recognize_google(audio) == 'hi bro':
                robot.say_text('whassup bro').wait_for_completed()
            if r.recognize_google(audio) == "nothing bro":
                robot.say_text('Thanks bro').wait_for_completed()
                break
            if r.recognize_google(audio) == 'find me events for today':
                robot.say_text (' okay please wait a sec bro!!').wait_for_completed()
                a = calendarday.findEvent('today')
                robot.say_text('there are ' + str(a) + 'events for today bro, for more information please go to the Url on my face')

        except sr.UnknownValueError:
            robot.say_text ("I am not understand what are you talking about").wait_for_completed()
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
cozmo.run_program(cozmo_program)
