import time,datetime,os
from multiprocessing import Pool

def getAirDrop(account, walletName, walletPass):
    logPrint("account: "+account+" start get airdrop...")
    
    os.system("cleos  -u https://publicapi-mainnet.eosauthority.com/ --wallet-url=http://localhost:8888 wallet unlock -n "
        + walletName + " --password " + walletPass)

    os.system("cleos  -u https://publicapi-mainnet.eosauthority.com/ --wallet-url=http://localhost:8888 \
               push action theeosbutton claimad '{\"account\":\"" + account + "\"}' -p " + account)
    
    logPrint("account: " + account + " airdrop done...")

def runInterval(interval,account, walletName, walletPass):
    while True:
        getAirDrop(account,walletName,walletPass)
        time.sleep(interval)

def logPrint(msg):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"+" "+msg))

if __name__ == '__main__':
    logPrint("start job...")
    p = Pool()

    #account one
    p.apply_async(runInterval, args=(5 * 60, "xxxx", "xxxxx", "xxxx",))

    # account two
    p.apply_async(runInterval, args=(5 * 60, "xxxxx", "xxxx", "xxxx",))
    
    p.close()
    p.join()
    logPrint("job done...")
