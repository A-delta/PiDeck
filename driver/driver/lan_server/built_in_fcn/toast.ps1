Param(
    [string]$title,
    [string]$content
)

[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")

$objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon

$objNotifyIcon.Icon = [System.Drawing.SystemIcons]::Information
$objNotifyIcon.BalloonTipIcon = "Info" 
$objNotifyIcon.BalloonTipTitle = $title 
$objNotifyIcon.BalloonTipText = $content
$objNotifyIcon.Visible = $True 
$objNotifyIcon.ShowBalloonTip(10000)