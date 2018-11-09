======================
GoFast : Known issues
======================


.. CAUTION:: If you subscribed for GoFAST Enterprise and you don`t find the answers to your questions below it is important (after checking that you follow pre-requirements) to provide some information to CEO-vision support about the type of software you use (Windows, Mac, Linux), operating system version, browser type and version, if necessary the version of the office suite (MS-Office, LibreOffice, ...). You can alsoconsult in the forum: https://community.ceo-vision.com

Office issues
================================================
Find out the version of the Office suite you use
------------------------------------------------
In case when an issue relates to the application of MS-Office suite it is important to know what kind of its version you have and if the updates are automatically installed. The Office version can be found "About Excel". For example, here is the version 1801

.. figure:: media-guide/trouver-version-excel.png

Notification “Impossible to connect to ... Please check the web address you use is correct".
--------------------------------------------------------
MS-Office does not support paths longer than 240 characters. For solving such issue you should do one of actions below:

- reduce the file name
- use either LibreOffice or OnlyOffice

The notification “The download failed”: It is impossible to save the file on Microsoft Office after an online edition.
------------------------------------------------------------------

During an online edition of an Office file, it may happen while saving, the notification indicates that the file is read-only and cannot be saved.

The problem is often caused by the malfunction of the “Microsoft Download Center”. This Download center is made to avoid losing your work in the event of disconnection with the remote server (For example: GoFAST). However, sometimes it blocks the upload of the files. These blocked files are listed on the Downloaded center.

There are two solutions to fix such issue:

1/ Instead of “Save”, choose “Save as”, then click on “Recent files” and select the folder where your file will be kept. Save your version overwriting the file which is on the server.

.. figure:: media-guide/MS_1.png
   :alt:

If Office tells you that saving cannot be done, follow the procedure below.

2/ The Microsoft Download Center sometimes blocks the downloading of a file and it blocks all following files. In this case, you must open the Download Center (orange icon in the task bar) and empty the list (see in the screenshots):

.. figure:: media-guide/Echec-de-telechargement.png
   :alt:
   
.. figure:: media-guide/MS_2.png
   :alt:
   
.. figure:: media-guide/MS_3.png
   :alt:
   
1/ If you send (download) the blocked versions into the list, overwrite the version that is on GoFAST with a version that may be outdated. Thus pay attention to the dates of update on GoFAST (history / documents’ versions).

.. NOTE:: Overwriting a file with a new version is reversible because everything is automatically versioned with GoFAST and you can reclaim old versions in just one click.

2/ If you delete/empty the list of documents in this Office Download Center, it is advisable to check that you have the final version of the file on your PC. If you have never saved your file on your PC, it is necessary to click on "Save Copy" on the most recent version in the Office Download Center.

When the blocked files have been deleted:

1/ Your file is opened in edition from GOFAST and you can return on the document into MS-Office (Word, Excel...) and re-click on "Save". The file is uploaded towards GOFAST.

2/ The file is on your PC (ex: Desktop) and you can drag and drop it from the PC to GoFAST, on the document page (upper right corner, dotted area).

Notification "Beware of the files from the Internet".
-----------------------------------------------------

If Office is configured in "Protected Mode" when editing online a message will bedisplayed "Beware of files from the Internet because they may contain viruses."

To avoid this notification: File / Option / Trust Center / Trust Center Settings / Trusted Locations

Check: "Allow approved locations on mynetwork" and "Add a new location"

.. figure:: media-guide/MS-Office-emplacement-approuvé.png
    :scale: 75%
    :align: center
    :alt: MS-Office-emplacement-approuvé
    
Microsoft Files Explorer Problem
================================
.. NOTE:: The Microsoft file explorer works more or less well depending on the versions of Windows you use. If you encounter persistent problems we advise you to install third-party software like Cyberduck https://cyberduck.io. Nevertheless in this case it is impossible to make "Open from" or "Save as" from Windows applications and specifying a GoFAST path.

The notification "Cannot save the file because its size is larger than the allowed size"
----------------------------------------------------------------------------------------
Such Windows notification comes from a limitation imposed by the Windows system, which prevents the transfer of large files by Webdav.

Notification “Network error” happens to Windows explorer (0x80070035)
----------------------------------------------------------------------

.. figure:: media-guide/erreur-réseau-webdav.png
   :alt:
   
In the case of "Windows cannot access ...", check that the service [webclient] has started.

The detail of the error 0x80070035: "The network path was not found"

The notification "The file size exceeds the allowed limit ..." (0x800700DF)
---------------------------------------------------------------------------

If the copied file exceeds 50MB, Microsoft displays an error notification of type "Error 0x800700DF: The file size exceeds the limit allowed and can not be saved. "

How to avoid this notification:

- request a registry change as proposed by Microsoft: https://support.microsoft.com/fr-fr/help/900900/folder-copy-error-message-when-downloading-a-file-that-is-larger-than
- use GoFAST File Browser
- use other file explorer than Microsoft's (eg CyberDuck)

Impossible to edit online PDF content with Acrobat Reader (v18)
===============================================================
Check that the Acrobat Reader application is already closed before launching the edition online. Such problem does not happen to FoxitReaderWeb conference / Web-conferencing

Web conference
=========================

.. CAUTION:: The web conference requires recent and functional hardware (PC and local network infrastructure and Internet).

.. NOTE:: The utilization of 4G allows having better speed and less port filtering than the utilization of a simple ADSL.We have found that using the same browser for all participants can significantly increase the quality, especially with FIREFOX v60 +

The Notification “Unfortunately something went wrong”
-------------------------------------
Check that the resources of your PC are not congested (Processor, Network), by pressing CTRL + ALT + Del then "Task Manager" and that your PC is powerful enough.

If this happens at the very beginning of the webconference, refresh the web page or click F5

No Web conferencing with Safari.
-------------------------------

The Safari support for the WebRTC protocol used by the Jitsi-Meet webconference component is fairly recent and does not work completely. We recommend you to use Chrome for Mac or possibly the Temasys plugin (not supported).

IE11: "You are using an incompatible version of IE"
---------------------------------------------------

It indicates that IE11 is in compatibility mode (and therefore works like IE7 / 8/9/10 dependingon what was chosen (see in following screenshot).

Remember: This is an often decision to keep compatibility with old applications that does not work with a recent version of IE (yet the only ones receiving security patches since Microsoft abandoned IE in favor of Edge)

For changing this mode, click on the gear wheel, "Development Tools" and change "User Agent String" by IE11 instead of IE10 (see in the screenshot).
