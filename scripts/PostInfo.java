package scripts;

import java.io.File;
import java.util.ArrayList;

/**
 * PostInfo
 */
public class PostInfo implements extract {
    private static ArrayList<String> posts = new ArrayList<>();

    public String extractFileName(String filename) {
        int start = filename.lastIndexOf('-') + 1;
        int end = filename.lastIndexOf('.');
        return filename.substring(start, end);
    }

    public PostInfo() {
        System.out.println("Do not forget to update the file list");
    }

    public void updatePostInfo() {
        File postPath = new File("/home/welt/Desktop/welts.xyz/_posts");
        String[] fileArray = postPath.list();
        for (String fileIter : fileArray) {
            posts.add(extractFileName(fileIter));
        }
    }

    public static void main(String[] args) {
        PostInfo postInfo = new PostInfo();
        postInfo.updatePostInfo();
        
        return;
    }
}