### Sample output of all scenario scipts

## scenario_01.sh
```

Scenario 01:
This is the most basic example. A camera card is copied to a travel drive and an ASC-MHL file is
created with hashes of all files on the card.

Step 1A: The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_01/A002R2EC
traversing […]Output/scenario_01/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_01/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155603_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155603_0001.ascmhl" to chain file

```
## scenario_01A.sh
```

Scenario 01A:
This is the most basic example, this time adding additional descriptive metadata.

Step 1A: The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive, and additional metadata is added to the
         ASC-MHL file.

$ asc-mhl.py verify -n "John Doe" -u jodo -c "This is a verification in scenario 01A" […]Output/scenario_01A/A002R2EC
traversing […]Output/scenario_01A/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_01A/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155604_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155604_0001.ascmhl" to chain file

```
## scenario_02.sh
```

Scenario 02:
In this scenario a copy is made, and then a copy of the copy. Two ASC-MHL are created during
this process, documenting the history of both copy processes.

Step 1A: The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_02/A002R2EC
traversing […]Output/scenario_02/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_02/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155604_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155604_0001.ascmhl" to chain file

Step 2A: The card is copied from the travel drive to a file server.
Step 2B: The files are verified on the file server.

$ asc-mhl.py verify […]Output/scenario_02/A002R2EC
traversing […]Output/scenario_02/A002R2EC
verifying chain […]Output/scenario_02/A002R2EC/asc-mhl/chain.txt
     MD5: ddbd9cdfa362bbeefcc557a93475720c verified  : A002R2EC_2019-10-11_155604_0001.ascmhl
verifying files against hashes from A002R2EC_2019-10-11_155604_0001.ascmhl
  xxhash: 0ea03b369a463d9d                 verified  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 verified  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 verified  : Sidecar.txt
writing […]Output/scenario_02/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155604_0002.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155604_0002.ascmhl" to chain file

```
## scenario_03.sh
```

Scenario 03:
In this scenario the first hashes are created using the xxhash format. Different hash formats
might be required by systems used further down the workflow, so the second copy is verified
against the existing xxhash hashes, and additional MD5 hashes can be created and stored during
that process on demand.

Step 1A: The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive by creating xxhash hashes.

$ asc-mhl.py verify […]Output/scenario_03/A002R2EC
traversing […]Output/scenario_03/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_03/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155604_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155604_0001.ascmhl" to chain file

Step 2A: The card is copied from the travel drive to a file server.
Step 2B: The files are verified on the file server, and additional ("secondary") MD5 hashes
         are created.

$ asc-mhl.py verify -h "MD5" […]Output/scenario_03/A002R2EC
traversing […]Output/scenario_03/A002R2EC
verifying chain […]Output/scenario_03/A002R2EC/asc-mhl/chain.txt
     MD5: a98f7b179a27d775e4ab74499d268b13 verified  : A002R2EC_2019-10-11_155604_0001.ascmhl
verifying files against hashes from A002R2EC_2019-10-11_155604_0001.ascmhl
  xxhash: 0ea03b369a463d9d                 verified  : Clips/A002C006_141024_R2EC.mov
     MD5: f5ac8127b3b6b85cdc13f237c6005d80 new       : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 verified  : Clips/A002C007_141024_R2EC.mov
     MD5: 614dd0e977becb4c6f7fa99e64549b12 new       : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 verified  : Sidecar.txt
     MD5: 6425c5a180ca0f420dd2b25be4536a91 new       : Sidecar.txt
writing […]Output/scenario_03/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155604_0002.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155604_0002.ascmhl" to chain file

```
## scenario_04.sh
```

Scenario 04:
Copying a folder to a travel drive and from there to a file server with a hash mismatch in
one file.

Step 1A: The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_04/A002R2EC
traversing […]Output/scenario_04/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_04/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155604_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155604_0001.ascmhl" to chain file

Step 2A: The card is copied from the travel drive to a file server. During the copy
         the file "Sidecar.txt" becomes corrupt (altered).
Step 2B: The files are verified on the file server.

$ asc-mhl.py verify […]Output/scenario_04/A002R2EC
traversing […]Output/scenario_04/A002R2EC
verifying chain […]Output/scenario_04/A002R2EC/asc-mhl/chain.txt
     MD5: 6fb97d7cc5308c02271c0260e8f2a08b verified  : A002R2EC_2019-10-11_155604_0001.ascmhl
verifying files against hashes from A002R2EC_2019-10-11_155604_0001.ascmhl
  xxhash: 0ea03b369a463d9d                 verified  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 verified  : Clips/A002C007_141024_R2EC.mov
! xxhash: d60ed728dc0b8d2c                 failed    : Sidecar.txt
ERROR: verification failed for 1 file(s)
writing […]Output/scenario_04/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155605_0002.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155605_0002.ascmhl" to chain file

```
## scenario_05.sh
```

Scenario 05:
Copying two camera mags to a `Reels` folder on a travel drive, and the entire `Reels` folder 
folder to a server.

Step 1A: The card A002 is copied to a travel drive.
Step 1B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_05/Reels/A002R2EC
traversing […]Output/scenario_05/Reels/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_05/Reels/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155605_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155605_0001.ascmhl" to chain file

Step 2A: The card A003 is copied to a travel drive.
Step 2B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_05/Reels/A003R2EC
traversing […]Output/scenario_05/Reels/A003R2EC
  xxhash: 52392f79a36d6571                 original  : Clips/A003C011_141024_R2EC.mov
  xxhash: 104a1844733bba51                 original  : Clips/A003C012_141024_R2EC.mov
  xxhash: e5dda75a353d8b34                 original  : Sidecar.txt
writing […]Output/scenario_05/Reels/A003R2EC/asc-mhl/A003R2EC_2019-10-11_155605_0001.ascmhl
appending chain generation for "A003R2EC_2019-10-11_155605_0001.ascmhl" to chain file

Step 3A: The entire folder `Reels` is copied from the travel drive to a file
         server.
Step 3B: An arbitrary file `Summary.txt` is added to the `Reels` folder.
Step 3C: The `Reels` folder is verified on the file server.

$ asc-mhl.py verify […]Output/scenario_05/Reels
traversing […]Output/scenario_05/Reels
verifying files against hashes from A002R2EC_2019-10-11_155605_0001.ascmhl
  xxhash: 0ea03b369a463d9d                 verified  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 verified  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 verified  : Sidecar.txt
writing […]Output/scenario_05/Reels/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155605_0002.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155605_0002.ascmhl" to chain file
verifying files against hashes from A003R2EC_2019-10-11_155605_0001.ascmhl
  xxhash: 52392f79a36d6571                 verified  : Clips/A003C011_141024_R2EC.mov
  xxhash: 104a1844733bba51                 verified  : Clips/A003C012_141024_R2EC.mov
  xxhash: e5dda75a353d8b34                 verified  : Sidecar.txt
writing […]Output/scenario_05/Reels/A003R2EC/asc-mhl/A003R2EC_2019-10-11_155605_0002.ascmhl
appending chain generation for "A003R2EC_2019-10-11_155605_0002.ascmhl" to chain file
  xxhash: b7219c53e6093233                 original  : Summary.txt
writing […]Output/scenario_05/Reels/asc-mhl/Reels_2019-10-11_155605_0001.ascmhl
appending chain generation for "Reels_2019-10-11_155605_0001.ascmhl" to chain file

```
## scenario_06.sh
```

Scenario 06:
Calculating and displaying directory hashes during verification. Folder hashes might be required
by systems used further down the workflow, so these hashes can be created "on the fly" from
hashes in the ASC-MHL files on demand.

Step 1A (imaginary): The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_06/A002R2EC
traversing […]Output/scenario_06/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_06/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155605_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155605_0001.ascmhl" to chain file

Step 2: The files are verified again, and folder hashes are calculated and displayed (folder
        hashes are created by concatenating the hashes of the contents of a directory and
        hashing that collected hash data).

$ asc-mhl.py verify -s -d […]Output/scenario_06/A002R2EC
traversing […]Output/scenario_06/A002R2EC
verifying chain […]Output/scenario_06/A002R2EC/asc-mhl/chain.txt
     MD5: 592f50fe9d78c4463401936b0f4cb22f verified  : A002R2EC_2019-10-11_155605_0001.ascmhl
verifying files against hashes from A002R2EC_2019-10-11_155605_0001.ascmhl
  xxhash: 0ea03b369a463d9d                 verified  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 verified  : Clips/A002C007_141024_R2EC.mov
d xxhash: 4c226b42e27d7af3                 directory : Clips
  xxhash: 3ab5a4166b9bde44                 verified  : Sidecar.txt
d xxhash: de755f773988d0cf                 directory : .

```
## scenario_07.sh
```

Scenario 07:
Writing extended attributes (xxattr) for files and folders during verification.

Hashes stored in extended attributes might be required by systems used further down the
workflow, so the hashes from the ASC-MHL file can also be written to extended attributes
on demand.

Step 1A: The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_07/A002R2EC
traversing […]Output/scenario_07/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_07/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155606_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155606_0001.ascmhl" to chain file

Step 2: Inspecting extended attributes - no hash attributes are set.

$ /usr/bin/xattr -r -l […]Output/scenario_07/A002R2EC | grep theasc.asc-mhl.


Step 3: The files are verified again, and hashes are written into the extended attributes of
        the files.

$ asc-mhl.py verify -s -wx […]Output/scenario_07/A002R2EC
traversing […]Output/scenario_07/A002R2EC
verifying chain […]Output/scenario_07/A002R2EC/asc-mhl/chain.txt
     MD5: ab85211e8ff8e5391a60a19d0714226d verified  : A002R2EC_2019-10-11_155606_0001.ascmhl
verifying files against hashes from A002R2EC_2019-10-11_155606_0001.ascmhl
  xxhash: 0ea03b369a463d9d                 verified  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 verified  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 verified  : Sidecar.txt

Step 4: Inspecting extended attributes again - hash attributes are now set.

$ /usr/bin/xattr -r -l […]Output/scenario_07/A002R2EC | grep theasc.asc-mhl.
[…]Output/scenario_07/A002R2EC/Clips/A002C006_141024_R2EC.mov: com.theasc.asc-mhl.xxhash: 0ea03b369a463d9d
[…]Output/scenario_07/A002R2EC/Clips/A002C007_141024_R2EC.mov: com.theasc.asc-mhl.xxhash: 7680e5f98f4a80fd
[…]Output/scenario_07/A002R2EC/Sidecar.txt: com.theasc.asc-mhl.xxhash: 3ab5a4166b9bde44

```
## scenario_08.sh
```

Scenario 08:
In this scenario a copy is made, and then a copy of the copy. During the second copy the ASC-MHL file
becomes corrupt (altered).

Step 1A: The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_08/A002R2EC
traversing […]Output/scenario_08/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_08/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155606_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155606_0001.ascmhl" to chain file

Step 2A: The card is copied from the travel drive to a file server. During the copy
         the ASC-MHL with generation 0001 becomes corrupt (altered).
Step 2B: The files are verified on the file server.

$ asc-mhl.py verify […]Output/scenario_08/A002R2EC
traversing […]Output/scenario_08/A002R2EC
verifying chain […]Output/scenario_08/A002R2EC/asc-mhl/chain.txt
!    MD5: c3f9f460a15f298d8088313666386d56 failed    : A002R2EC_2019-10-11_155606_0001.ascmhl
ERROR: verification failed for 1 ascmhl file(s), didn't verify files

```
## scenario_09.sh
```

Scenario 09:
In this scenario two copies are made, while the first MHL file is digitally signed.
The signature gets checked afterwards.

Step 1A: The card is copied to a travel drive.
Step 1B: The files are verified on the travel drive, the ASCMHL file gets signed with
         a private key.

$ asc-mhl.py verify -csi abc@example.com -csp […]Template/Material/Scenario09/abc-private-key.pem […]Output/scenario_09/A002R2EC
traversing […]Output/scenario_09/A002R2EC
  xxhash: 0ea03b369a463d9d                 original  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 original  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 original  : Sidecar.txt
writing […]Output/scenario_09/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155607_0001.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155607_0001.ascmhl" with signature for abc@example.com to chain file

Step 2A: The card is copied again.
Step 2B: The files are verified on the travel drive.

$ asc-mhl.py verify […]Output/scenario_09/A002R2EC
traversing […]Output/scenario_09/A002R2EC
verifying chain […]Output/scenario_09/A002R2EC/asc-mhl/chain.txt
     MD5: e92ef9ac6b7174023b41e005622d9a7f verified  : A002R2EC_2019-10-11_155607_0001.ascmhl (signed by abc@example.com)
verifying files against hashes from A002R2EC_2019-10-11_155607_0001.ascmhl
  xxhash: 0ea03b369a463d9d                 verified  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 verified  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 verified  : Sidecar.txt
writing […]Output/scenario_09/A002R2EC/asc-mhl/A002R2EC_2019-10-11_155607_0002.ascmhl
appending chain generation for "A002R2EC_2019-10-11_155607_0002.ascmhl" to chain file

Step 3A: The chain is verified.

$ asc-mhl.py verify -s […]Output/scenario_09/A002R2EC
traversing […]Output/scenario_09/A002R2EC
verifying chain […]Output/scenario_09/A002R2EC/asc-mhl/chain.txt
     MD5: e92ef9ac6b7174023b41e005622d9a7f verified  : A002R2EC_2019-10-11_155607_0001.ascmhl (signed by abc@example.com)
     MD5: d811d8a654e1bbb9d3a9af9ec1505fe1 verified  : A002R2EC_2019-10-11_155607_0002.ascmhl
verifying files against hashes from A002R2EC_2019-10-11_155607_0001.ascmhl
  xxhash: 0ea03b369a463d9d                 verified  : Clips/A002C006_141024_R2EC.mov
  xxhash: 7680e5f98f4a80fd                 verified  : Clips/A002C007_141024_R2EC.mov
  xxhash: 3ab5a4166b9bde44                 verified  : Sidecar.txt

Step 3B: The signature is checked with a public key.

$ asc-mhl.py checksignature -g 1 -csp […]Template/Material/Scenario09/abc-public-key.pem […]Output/scenario_09/A002R2EC
checking signature for generation 1
     MD5: e92ef9ac6b7174023b41e005622d9a7f sig ok    : A002R2EC_2019-10-11_155607_0001.ascmhl (signed by abc@example.com)

```

The ASC-MHL files can be found in the ``asc-mhl`` folders amongst the scenario output files in the [Output/](Output/) folder.
