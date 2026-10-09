
class PARENT:
    Asset1 = "3BHK house"
    Asset2 = "Audi car"

    def parentMtd(self):
        print("This is the method from parent class")
        print("Asset1:", self.Asset1)
        print("Asset2:", self.Asset2)


class child(PARENT):
    Asset3 = "New House"

    def childMtd(self):
        print("\nAssets of parent inherited by child")
        print("Asset1:", self.Asset1)
        print("Asset2:", self.Asset2)
        print("Asset3", self.Asset3)


c = child()
c.parentMtd()
c.childMtd()

