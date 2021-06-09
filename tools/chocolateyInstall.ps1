$packageArgs = @{
    packageName = 'ObinsKit'
    fileType = 'exe'
    url64          = "https://s2.hexcore.xyz/occ/win32/x64/ObinsKit_1.1.5_x64.exe"
    checksum64     = "4aa001be2f9384bdb18fcb93f751d7f56f3b294db50a7f7ac272d0d6ef60b1f4"
    url            = "https://s2.hexcore.xyz/occ/win32/ia32/ObinsKit_1.1.5_ia32.exe"
    checksum       = "e50e7ceeca2667785d3cd2f738fa9520b98ebeab2f3fdd55feef7bbdfda4b71c"
    checksumType  = 'sha256'
    checksumType64  = 'sha256'
    silentArgs    = "/S"
  }

Install-ChocolateyPackage @packageArgs