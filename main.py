import enumerator

if __name__ == "__main__":
    packets = set()
    start = enumerator.start_stamp
    while start < enumerator.end_stamp:
        packets.update(enumerator.GetPackages(start))
        start += enumerator.step
        print(start)
    print(len(packets))
    f = open("go_packages.txt", "w")
    f.write("\r\n".join(packets))
    f.close()