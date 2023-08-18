import subprocess

def commandline(katanga, app):

	cmd = str(f"{katanga} " + "--game-path" + f"{app} " + "--launch-type DX11Exe")
	result = subprocess.call(cmd, shell=True)
	return result

if __name__ == '__main__':
	katanga = r"F:\SteamLibrary\steamapps\common\HelixVision\Tools\Katanga\katanga.exe"
	app = r"F:\SteamLibrary\steamapps\common\PUBG\TslGame\Binaries\Win64\TslGame_UC.exe"
	commandline(katanga, app)



'''
Note:

PowerShell CLI parameters used:

-# NoProfile isn't strictly necessary, but advisable, because it suppresses loading of PowerShell's profiles, which can both help performance and makes for a predictable execution environment.
-Command isn't strictly necessary with powershell.exe, the Windows PowerShell CLI, as it is the implied default; however, it is necessary if you call the PowerShell (Core) 7+ CLI, pwsh.exe, which now defaults to -File instead.
The PowerShell code used to extract the links:

Since your script invokes an external program, 7z.exe, that program's stdout is reported line by line by PowerShell.
When the regex-based -match operator is given an array as its LHS operand, it acts as a filter. Therefore, only those lines that start with (^) string https:// are returned.
Share
'''