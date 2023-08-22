import java.util.ArrayList;
import java.util.List;

class Manacher {
    private String t;
    private List<Integer> p;

    private int lpsStart, lpsLength;

    public Manacher(String s) {
        t = "";
        for (char i : s.toCharArray()) {
            t += "#" + i;
        }
        t += "#";

        build();
    }

    private void build() {
        int n = t.length();
        p = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            p.add(1);
        }

        int l = 1, r = 1;

        for (int i = 1; i < n; i++) {
            if (l + r - i >= 0) p.set(i, Math.max(1, Math.min(r - i, p.get(l + r - i))));

            while (i - p.get(i) >= 0 && i + p.get(i) < n && t.charAt(i - p.get(i)) == t.charAt(i + p.get(i))) {
                p.set(i, p.get(i) + 1);
            }

            if (i + p.get(i) > r) {
                l = i - p.get(i);
                r = i + p.get(i);

                if (lpsLength < p.get(i)) {
                    lpsStart = l + 2;
                    lpsLength = p.get(i) - 1;
                }
            }
        }
    }

    private int getLongest(int center, boolean odd) {
        int position = 2 * center + 1 + (odd ? 1 : 0);
        return p.get(position) - 1;
    }

    public boolean checkPalindrome(int l, int r) {
        if ((r - l + 1) <= getLongest((l + r) / 2, (r - l + 1) % 2 == 1)) {
            return true;
        }
        return false;
    }

    public String longestPalindromeSubstring() {
        int n = t.length();
        StringBuilder ans = new StringBuilder();
        for (int i = lpsStart; i < n && lpsLength > 0; i += 2) {
            ans.append(t.charAt(i));
            lpsLength--;
        }
        return ans.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        String input = "babbabbabc";
        Manacher solution = new Manacher(input);
        String result = solution.longestPalindromeSubstring();
        System.out.println("Longest palindrome substring: " + result);
    }
}
