def locateClusters(fat, key):
    if fat[key] == 0:
        fat.pop(key)
    else:
        nextKey = fat[key]
        fat.pop(key)
        locateClusters(fat, nextKey)

def main():
    # creates a list called "rootDir" and prints it out so that the user can see it.
    rootDir = []
    rootLen = int(input("Enter number of elements in the root directory: "))
    for _ in range(0, rootLen):
        ele = int(input("Enter elements: "))
        rootDir.append(ele)
    print(rootDir)

    # creates a dictionary called "fat" and prints it out so that the user can see it.
    fatLen = int(input("Enter the number of elements in the FAT Table: "))
    fat = {}
    for _ in range(fatLen):
        keys = int(input())
        values = int(input())
        fat[keys] = values
    print(fat)

    # calls the "locateClusters" method using the number of elements in the list "rootDir"
    for x in rootDir:
        locateClusters(fat, x)
    
    # calls the "findLocations" method and prints the results to the user.
    print("Locations of file(s) are:")
    local = fat.keys()
    print(list(local))

main()