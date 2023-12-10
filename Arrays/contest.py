class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        testedDevice=0
        minValue=0
        lengthOfBatteries=len(batteryPercentages)
        for i in range(0,lengthOfBatteries):
            if batteryPercentages[i]>0:
                testedDevice+=1
                for j in range(i+1,lengthOfBatteries):
                    batteryPercentages[j]=max(minValue,batteryPercentages[j]-1)
                    print(batteryPercentages)
        return testedDevice
        
res=Solution.countTestedDevices(any,[1,1,2,1,3])
print(res)
print("-------")
res=Solution.countTestedDevices(any,[0,1,2])
print(res)
 