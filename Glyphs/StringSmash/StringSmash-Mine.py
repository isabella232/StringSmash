#MenuTitle: StringSmash Mine
# -*- coding: utf-8 -*-

__doc__ = '''
StringSmash is a simple RoboFont extension/Glyphs App script to generate strings
for spacing/kerning.
'''

# system
from vanilla import *
import os
import datetime
import re

# Glyphs
import GlyphsApp
import getpass
from PyObjCTools.AppHelper import callAfter

# presets
import StringSmashDicts
import importlib
importlib.reload(StringSmashDicts)


class StringSmash(object):
    '''Returns string'''

    delimL = []
    listL = []
    inputListL = []
    listR = []
    inputListR = []
    delimR = []
    flip = False
    trio = False
    space = True
    replace = False
    sortBy = 0 # sort by lGlyph

    flipEnabled = True
    trioEnabled = True

    # diff
    if Glyphs.font:
        f = Glyphs.font
        font = []
        for i in f.glyphs:
            font.append(i.name)
    else:
        font = []


    def __init__(self):
        windowWidth = 300

        '''A simple GUI'''
        self.w = FloatingWindow((-360, 40, windowWidth, 358), "StringSmash v.1.0 Mine", textured=False, autosaveName = "com.belafrank.StringSmash.mainwindow")

        # list selections
        presetListL = sorted(StringSmashDicts.presetDictL.keys())
        presetListR = sorted(StringSmashDicts.presetDictR.keys())
        delimList = sorted(StringSmashDicts.delimDict.keys())

        popUpLists = [
            ['-'] + delimList, # delimL
            ['-'] + presetListL, # listL
            ['-'] + presetListR, # listR
            ['-'] + delimList, # delimR
        ]

        # input text
        totalBoxYPos = 50
        textBoxYPos = [50+18+5, 85+18+24+5]
        textBoxNames = ['listLExtra', 'listRExtra']
        for i, textBox in enumerate(textBoxNames):
            EditTextBox = EditText((30, textBoxYPos[i], 180, 24), callback=self.inputPreset)
            EditTextBox.var = textBox
            setattr(self.w, textBox, EditTextBox)

        # pick preset popup
        yPos = [15, 50, 85+24, 120+totalBoxYPos]
        names = ['delimL', 'listL', 'listR', 'delimR']
        presets = [delimList, presetListL, presetListR, delimList]
        dictList = [StringSmashDicts.delimDict, StringSmashDicts.presetDictL, StringSmashDicts.presetDictR, StringSmashDicts.delimDict]
        changeThis = ['', '', '', '']
        x = 0
        for i in names:
            popupButton = PopUpButton((30, yPos[x], 180, 18),
                popUpLists[x], sizeStyle='regular', callback=self.pickPreset)
            popupButton.var = i
            popupButton.pickFrom = presets[x]
            popupButton.dict = dictList[x]
            setattr(self.w, i, popupButton)

            # get selection buttons
            squareButton = SquareButton((220, yPos[x], -10, 20), 'Get', sizeStyle='regular',
                callback=self.getSelection)
            squareButton.var = i
            setattr(self.w, 'button_%s' %i, squareButton)

            x += 1

        # radio groups
        radioGroup = RadioGroup((5, 31, 26, 68+totalBoxYPos),
                                ["", ""],
                                sizeStyle = "regular",
                                callback=self.setSortBy)
        if Glyphs.defaults[ "com.belafrank.StringSmash.sortBy" ] != "":
            try:
                radioGroup.set( Glyphs.defaults[ "com.belafrank.StringSmash.sortBy"] ) # load preference UI
            except:
                radioGroup.set(0)
        else:
            radioGroup.set(0)
        setattr(self.w, 'radio_sortBy', radioGroup)


        # check marks for input text
        self.w.checkMarkL = TextBox((220, textBoxYPos[0], -10, 17), "")
        self.w.checkMarkR = TextBox((220, textBoxYPos[1], -10, 17), "")


        # checkboxes
        xPos = [15, 80, 145, 220]
        yPos = 165+totalBoxYPos
        titles = ['Flip', 'Trio', 'Space', 'Replace']
        values = [False, False, True, False]
        # Load preferences for UI
        values[2:] = [Glyphs.defaults[ "com.belafrank.StringSmash.%s"%title] if Glyphs.defaults[ "com.belafrank.StringSmash.%s"%title] != "" else defaultValues[i] for title in ['space', 'replace']]
        x = 0
        for i in titles:
            checkBox = CheckBox((xPos[x], yPos, -10, 20), titles[x], sizeStyle='regular', value=values[x], callback=self.swithFlipTrio)
            temp = [0, 0, 0, 0]
            temp[x] = 1
            checkBox.var = temp
            setattr(self.w, 'checkBox_%s' %i, checkBox)
            x += 1


        # generate buttons
        names = ['Generate and Open', 'Generate and Copy', 'Save String', 'Save MM style']
        callbackNames = ['generateAndOpen', 'generateAndCopy', 'saveString', 'saveMmStyle']
        callbacks = [self.button_generateAndOpen, self.button_generateAndCopy,
            self.button_saveString, self.button_saveMmStyle]
        vSpace = 5
        genButtonWidth = (windowWidth-vSpace*5)/2
        xPos = [vSpace*2, vSpace*3+genButtonWidth, vSpace*2, vSpace*3+genButtonWidth]
        yPos = [210, 210, 255, 255]
        yPos = [y + totalBoxYPos for y in yPos]
        height = 40
        x = 0
        for i in names:
            button = SquareButton((xPos[x], yPos[x], genButtonWidth, height), i, sizeStyle='regular',
                callback=callbacks[x] )
            setattr(self.w, 'button_%s' %callbackNames[x], button)
            x += 1


        # horizontal dividers
        yPos = [155, 195]
        yPos = [y + totalBoxYPos for y in yPos]
        for i in yPos:
            horizontalLine = HorizontalLine((0, i, -0, 1))
            setattr(self.w, 'horizontalLine_%i' %i, horizontalLine)

        # self.w.verticalLine = VerticalLine((170, 161, 1, 50))


        self.LoadPreferences(dictList)
        self.w.open()


    def swithFlipTrio(self, sender):
        if sender.var[0:2] == [1, 0]:
            if self.flip == True:
                self.flip = False
            else:
                self.flip = True
            if self.trioEnabled == True:
                self.w.checkBox_Trio.enable(False)
                self.trioEnabled = False
            else:
                self.w.checkBox_Trio.enable(True)
                self.trioEnabled = True

        if sender.var[0:2] == [0, 1]:
            if self.trio == True:
                self.trio = False
            else:
                self.trio = True
            if self.flipEnabled == True:
                self.w.checkBox_Flip.enable(False)
                self.flipEnabled = False
            else:
                self.w.checkBox_Flip.enable(True)
                self.flipEnabled = True

        if sender.var[2] == 1: # space
            if self.space == True:
                self.space = False
            else:
                self.space = True
            Glyphs.defaults["com.belafrank.StringSmash.space"] = self.w.checkBox_Space.get() # save preference variable

        if sender.var[3] == 1: # replace
            if self.replace == True:
                self.replace = False
            else:
                self.replace = True
            Glyphs.defaults["com.belafrank.StringSmash.replace"] = self.w.checkBox_Replace.get() # save preference variable


    def setSortBy(self, sender):
        if sender.get() == 0: 
            self.sortBy = 0 # sort by lGlyph
        elif sender.get() == 1:
            self.sortBy = 1 # sort by rGlyph
        Glyphs.defaults["com.belafrank.StringSmash.sortBy"] = self.w.radio_sortBy.get() # save preference variable


    def LoadPreferences(self, dictList):
        loadList = ["delimL", "listL", "listR", "delimR", ["space", "checkBox_Space"], ["replace", "checkBox_Replace"], ["sortBy", "radio_sortBy"]]
        for i, Load in enumerate(loadList):
            if i < 4:
                try: # Load preferences UI and variables
                    exec("""self.w.{0}.set( Glyphs.defaults[ "com.belafrank.StringSmash.{0}" ] )\nif self.w.{0}.get() > 0:\n    self.{0} = self.w.{0}.dict[self.w.{0}.pickFrom[self.w.{0}.get() - 1]]\nelse:\n  self.{0} = []\n""".format(Load))
                except Exception as e:
                    Glyphs.showMacroWindow()
                    print("\n⚠️ Script Error:\n")
                    import traceback
                    print(traceback.format_exc())
                    print()
                    raise e
            if i >= 4:
                try: # Load preferences variables
                    #self.w.{1}.set( Glyphs.defaults[ "com.belafrank.StringSmash.{0}" ] )\n
                    exec("""self.{0} = self.w.{1}.get()""".format(Load[0], Load[1]))
                except Exception as e:
                    Glyphs.showMacroWindow()
                    print("\n⚠️ Script Error:\n")
                    import traceback
                    print(traceback.format_exc())
                    print()
                    raise e


    def pickPreset(self, sender):
        '''...'''
        # get the list items
        if sender.get() > 0:
            i = sender.get() - 1
            dictKey = sender.pickFrom[i]
            temp = sender.dict[dictKey]
        else:
            temp = []

        # pass it to list
        if sender.var == 'delimL':
            self.delimL = temp
            Glyphs.defaults["com.belafrank.StringSmash.delimL"] = sender.get() # save preference variable
        elif sender.var == 'delimR':
            self.delimR = temp
            Glyphs.defaults["com.belafrank.StringSmash.delimR"] = sender.get() # save preference variable
        elif sender.var == 'listL':
            self.listL = temp
            Glyphs.defaults["com.belafrank.StringSmash.listL"] = sender.get() # save preference variable
        elif sender.var == 'listR':
            self.listR = temp
            Glyphs.defaults["com.belafrank.StringSmash.listR"] = sender.get() # save preference variable
        else:
            pass


    def inputPreset(self, sender):
        inputText = str(sender.get())
        if sender.var == 'listLExtra':
            self.inputListL = inputText.split(" ")
            if all(eachKey in StringSmashDicts.presetDictL for eachKey in self.inputListL):
                self.w.checkMarkL.set(u"✓")
            else:
                self.w.checkMarkL.set(u"?")
        elif sender.var == 'listRExtra':
            self.inputListR = inputText.split(" ")
            if all(eachKey in StringSmashDicts.presetDictR for eachKey in self.inputListR):
                self.w.checkMarkR.set(u"✓")
            else:
                self.w.checkMarkR.set(u"?")


    # diff
    def getSelection(self, sender):
        if Glyphs.font:
            temp = []
            f = Glyphs.font
            if f.selectedLayers:
                for g in [ l.parent.name for l in f.selectedLayers if l.parent.name != None]:
                    if g != "space":
                        temp.append(g)

            if sender.var == 'delimL':
                self.delimL = temp
                self.w.delimL.set(0)
            elif sender.var == 'delimR':
                self.delimR = temp
                self.w.delimR.set(0)
            elif sender.var == 'listL':
                self.listL = temp
                self.w.listL.set(0)
            elif sender.var == 'listR':
                self.listR = temp
                self.w.listR.set(0)
            else:
                pass

        else:
            pass


    def button_generateAndOpen(self, sender):
        theString = self.generateString(self.listL, self.listR, self.delimL, self.delimR, self.flip, self.trio, self.space, self.sortBy, True)

        if theString != '':
            if self.replace == False:
                self.openTab(theString)
            elif self.replace == True:
                self.replaceTab(theString)
        else:
            pass


    def button_generateAndCopy(self, sender):
        theString = self.generateString(self.delimL, self.delimR, self.listL, self.listR, self.flip, self.trio, self.space, self.sortBy, False)

        if theString != '':
            os.system('echo "%s" | pbcopy' % theString) # copy to Clipboard, neat
        else:
            pass


    def button_saveString(self, sender):
        theString = self.generateString(self.delimL, self.delimR, self.listL, self.listR, self.flip, self.trio, self.space, self.sortBy, False)

        if theString != '':
            self.saveFile('StringSmash_', theString)
        else:
            pass


    def button_saveMmStyle(self, sender):
        listL = self.listL+self.getAllInputListItems(self.inputListL, "L")
        listR = self.listR+self.getAllInputListItems(self.inputListR, "R")

        if self.sortBy == 0: # sort by lGlyph
            aList = [x + ' ' + y for x in listL for y in listR]
        elif self.sortBy == 1: # sort by rGlyph
            aList = [x + ' ' + y for y in listR for x in listL]

        if self.flip == True: # flip
            bothLists = self.flipListMaker(aList)
            aList = bothLists

        theString = '\n'.join(aList)

        if theString != '':
            theString = '#KPL:P: Generated with StringSmash\n' + theString
            self.saveFile('StringSmash_MM_', theString)
        else:
            pass


    def makeTimeStamp(self):
        mark = str(datetime.datetime.now())
        mark = mark.replace('-', '')
        mark = mark.replace(' ', '')
        mark = mark.replace(':', '')
        mark = mark.replace('.', '')
        return mark


    # diff
    def saveFile(self, name, content):
        if Glyphs.font:
            aDir, aFile = os.path.split(Glyphs.font.filepath)
        else:
            aDir = os.path.expanduser('~/Desktop')
            # should offer to select a folder

        stamp = self.makeTimeStamp()
        path = aDir + '/' + name + stamp + '.txt'

        aFile = open(path, 'w')
        aFile.write(content)
        aFile.close()


    # diff
    def openTab(self, aString):
        callAfter( Glyphs.currentDocument.windowController().addTabWithString_, aString )

    def replaceTab(self, aString):
        TextStoreage = Glyphs.currentDocument.windowController().activeEditViewController().graphicView().textStorage()
        String = TextStoreage.text().string()
        Range = Glyphs.currentDocument.windowController().activeEditViewController().graphicView().selectedRange()
        Range.location = 0 # Replace all text
        Range.length = len(String) # Replace all text
        charString = Glyphs.font.charStringFromDisplayString_(aString)
        TextStoreage.replaceCharactersInRange_withString_(Range, charString)

    ''' this is what needed to successfully generate a string
    the original version was completely refactored, it works now
    '''

    def makeString(self, aList, aString, bString, space):
        '''Makes /A strings using given list's members'''
        pairList = [aString + '/' + a + bString + space for a in aList]
        return ''.join(pairList)


    def makePairString(self, aList, bList, aString, bString, space, sortBy):
        '''Returns /A/B strings using given lists's members'''
        if sortBy == 0: # sort by lGlyph
            pairList = [aString + '/' + a + '/' + b + bString + space for a in aList for b in bList]
        elif sortBy == 1: # sort by rGlyph
            pairList = [aString + '/' + a + '/' + b + bString + space for b in bList for a in aList]
        return ''.join(pairList)


    # Reverse 'left' with 'right' when making a flipped list
    def flipListMaker(self, aList):
        print("aList", aList)
        aFlippedList = []
        for eachItem in aList:
            # if this is used just for MM then ok otherwise:
            # need to make this work for non 'spacing', split up pairList into tuples ('a', 'b') then join, need to consider delimiters
            [l, r] = eachItem.split(" ")
            if "left" in l:
                l = l.replace("left", "right")
            if "right" in r:
                r = r.replace("right", "left")
            aFlippedList += ["{1} {0}".format(l,r)]
        bothLists = [item for sublist in zip(aList,aFlippedList) for item in sublist]
        print("bothLists", bothLists)
        return bothLists


    def makeFlipPairString(self, aList, bList, aString, bString, space, sortBy):
        '''Returns /A/B/A/B strings using given lists's members'''
        ## Classic non /quoteleft/A /A/quoteright method
        # pairList = [aString + '/' + a + '/' + b + bString + space + aString + '/' + b + '/' + a + bString + space for b in bList for a in aList]
        if sortBy == 0: # sort by lGlyph
            pairList = [aString + '/' + a + '/' + b + bString + space + aString + '/' + b.replace("right", "left") + '/' + a.replace("left", "right") + bString + space for a in aList for b in bList]
        elif sortBy == 1: # sort by rGlyph
            pairList = [aString + '/' + a + '/' + b + bString + space + aString + '/' + b.replace("right", "left") + '/' + a.replace("left", "right") + bString + space for b in bList for a in aList]
        return ''.join(pairList)


    def makeTrioString(self, aList, bList, aString, bString, space):
        '''Returns /A/B/A strings using given lists's members'''
        # pairList = [aString + '/' + a + '/' + b +'/' + a + bString + space for b in bList for a in aList]
        # Make Flip Trio ie /quoteleft/a/quoteright
        pairList = [aString + '/' + a + '/' + b +'/' + a.replace("left", "right") + bString + space for b in bList for a in aList]
        return ''.join(pairList)


    def subsetList(self, aList, bList):
        '''Returns section of two lists—keeps original order of first
        this better use this than 'sets' if you need the original order'''
        temp = [a for a in aList if a in bList]
        return temp


    def removeEmptyString(self, aList):
        '''Removes empty string elements from list'''
        newList = [a for a in aList if a != '']
        return newList


    def listToString(self, aList):
        '''Convert delimiter list to delimiter string'''
        if len(aList) == 0:
            return ''
        if len(aList) == 1:
            return '/' + aList[0]
        if len(aList) > 1:
            return '/' + '/'.join(aList)


    def getAllInputListItems(self, inputList, side):
        allItems = []
        if side == "L":
            presetDict = StringSmashDicts.presetDictL
        elif side == "R":
            presetDict = StringSmashDicts.presetDictR
        for eachList in inputList:
            try:
                allItems += presetDict[eachList]
            except Exception as e:
                Glyphs.showMacroWindow()
                print("\n⚠️ Script Error:\n")
                import traceback
                print(traceback.format_exc())
                print()
                raise e
        return allItems


    def generateString(self, listL, listR, delimL, delimR, flip, trio, space, sortBy, subset):
        '''This generates strings'''

        if subset == True:
            # subset lists
            listL =  self.subsetList(self.listL+self.getAllInputListItems(self.inputListL, "L"), self.font)
            listR =  self.subsetList(self.listR+self.getAllInputListItems(self.inputListR, "R"), self.font)
            delimL = self.subsetList(self.delimL, self.font)
            delimR = self.subsetList(self.delimR, self.font)

            delimL =  self.listToString(self.removeEmptyString(delimL))
            delimR =  self.listToString(self.removeEmptyString(delimR))
        else:
            listL = self.listL+self.getAllInputListItems(self.inputListL, "L")
            listR = self.listR+self.getAllInputListItems(self.inputListR, "R")
            delimL = self.delimL
            delimR = self.delimR

            delimL =  self.listToString(self.removeEmptyString(delimL))
            delimR =  self.listToString(self.removeEmptyString(delimR))

        spaceChar = ""
        space = self.space
        if space:
            spaceChar = "  "

        # both empty list
        if not listL and not listR:
            return 'Both is empty'

        # neither list is empty
        elif listL and listR:
            if trio:
                return self.makeTrioString(listL, listR, delimL, delimR, spaceChar)
            if flip:
                return self.makeFlipPairString(listL, listR, delimL, delimR, spaceChar, sortBy)
            else:
                return self.makePairString(listL, listR, delimL, delimR, spaceChar, sortBy)

        # both empty list
        elif not listL and not listR :
            return ''

        # first list is an empty list
        elif listL == []:
            listL = ['']
            listL, listR = listR, listR
            return self.makeString(listL, delimL, delimR, spaceChar)

        # second list is an empty list
        elif listR == []:
            listR = ['']
            return self.makeString(listL, delimL, delimR, spaceChar)

        else:
            return 'No string at all'

StringSmash()