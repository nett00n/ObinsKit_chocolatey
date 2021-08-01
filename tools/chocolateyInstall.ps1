$packageArgs = @{
    packageName = 'ObinsKit'
    fileType = 'exe'
    url64          = "https://s3.hexcore.xyz/occ/win32/x64/ObinsKit_1.1.8_x64.exe"
    checksum64     = "5f1b4708b75f5952e5bf3f237bf7dbcb708e3f91a4f03588c2dceb1a69bf3509"
    url            = "https://s3.hexcore.xyz/occ/win32/ia32/ObinsKit_1.1.8_ia32.exe"
    checksum       = "248aeaaf2527cd08e36192016c5a0d68846edddb173740e13d1a9ee7452be9c8"
    checksumType  = 'sha256'
    checksumType64  = 'sha256'
    silentArgs    = "/S"
  }

Install-ChocolateyPackage @packageArgs