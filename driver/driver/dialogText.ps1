Param(
    [string]$ttl,
    [string]$text
)

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

$GUI                             = New-Object system.Windows.Forms.Form
$GUI.ClientSize                  = New-Object System.Drawing.Point(379,99)
$GUI.text                        = $ttl
$GUI.TopMost                     = $false
$GUI.Icon                        = "C:\Program Files\RaspiMote\logo\RaspiMote_logo.ico"

$Title                           = New-Object system.Windows.Forms.Label
$Title.text                      = $text
$Title.AutoSize                  = $true
$Title.width                     = 25
$Title.height                    = 10
$Title.location                  = New-Object System.Drawing.Point(19,17)
$Title.Font                      = New-Object System.Drawing.Font('Open Sans',10)

$TextBox1                        = New-Object system.Windows.Forms.TextBox
$TextBox1.multiline              = $false
$TextBox1.width                  = 180
$TextBox1.height                 = 20
$TextBox1.location               = New-Object System.Drawing.Point(80,50)
$TextBox1.Font                   = New-Object System.Drawing.Font('Open Sans',10)

$Button1                         = New-Object system.Windows.Forms.Button
$Button1.text                    = "Validate"
$Button1.width                   = 80
$Button1.height                  = 30
$Button1.location                = New-Object System.Drawing.Point(280,59)
$Button1.Font                    = New-Object System.Drawing.Font('Open Sans',10)


$GUI.controls.AddRange(@($Title,$TextBox1,$Button1))

$Button1.Add_Click(
    {
       Write-Output $TextBox1.text > $env:USERPROFILE\AppData\Roaming\RaspiMote\tmp\dialogTextOutput.txt
       $GUI.close()
    }
)

$GUI.ShowDialog()