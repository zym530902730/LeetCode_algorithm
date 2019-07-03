import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Title: ContainsDuplicate
 * ProjectName: leetcode-java
 * Function:  TODO
 * author     Yiming Zhao
 * Date:      2019-06-05 23:41
 */
public class ContainsDuplicate_217 {
    public boolean containsDuplicate(int[] nums) {
        //先排序，在遍历一次
        //执行用时 : 8 ms, 在Contains Duplicate的Java提交中击败了88.65% 的用户
        //内存消耗 : 46.2 MB, 在Contains Duplicate的Java提交中击败了80.21% 的用户
        int len=nums.length;
        Arrays.sort(nums);
        if(len<=1){
            return false;
        }
        for(int i=0;i<len-1;i++){
            if(nums[i]==nums[i+1]){
                return true;
            }
        }
        return false;
    }
    // 使用set去重
    // 执行用时 :9 ms, 在所有 Java 提交中击败了87.02%的用户
    // 内存消耗 :48.4 MB, 在所有 Java 提交中击败了80.15%的用户
    public boolean containsDuplicate2(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        for (int i : nums) {
            set.add(i);
        }
        return nums.length == set.size() ? false : true;
    }


}
