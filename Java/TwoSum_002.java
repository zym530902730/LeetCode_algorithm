import java.util.HashMap;
import java.util.Map;

/**
 * Title: TwoSum
 * ProjectName: leetcode-java
 * Function:  TODO
 * author     Yiming Zhao
 * Date:      2019-06-05 22:25
 */
public class TwoSum_002 {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[] { i, map.get(complement)};
            }
        }
        throw new IllegalArgumentException("No two sm solution");
    }

    public int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)){
                return new int[] {map.get(complement),i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }


}

