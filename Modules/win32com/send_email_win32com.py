# https://www.youtube.com/watch?v=4AMsBrkkH00

import win32com.client as win32

olApp = win32.Dispatch("Outlook.Application")
olNS = olApp.GetNameSpace("MAPI")

mailItem.olApp.CreateItem(0)
mailItem.Subject = "Hello"
mailItem.BodyFormat = 1
mailItem.Body = "Hello Body"
mailItem.To = "jinhodavid.seo@nyct.com"
mailItem._Oleobj_.Invoke("")
