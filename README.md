# crypto-address-balance-checker
*Check balance of huge list of addresses.*

To use this script you need first to create 'addr.txt' file with list of addresses.

Depending of which crypto coin you check, change explorer link in 'EXPLORER' veriable (Recently Teloscoin).

Run script by:
```
python3 checker.py
```
### You will be asked to choose option 1 or 2.

**Option 1**, will read one by one all addresses from 'addr.txt' file, check their balance on explorer and write data into database.
![Image1](https://raw.githubusercontent.com/luxleather/crypto-address-balance-checker/main/Screenshot%20from%202020-12-13%2014-05-48.png)



**Option 2**, will read database and display all addresses with their balances.
![Image2](https://raw.githubusercontent.com/luxleather/crypto-address-balance-checker/main/Screenshot%20from%202020-12-13%2014-06-18.png)
