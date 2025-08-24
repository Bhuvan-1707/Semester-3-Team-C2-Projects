#include<time.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/stat.h>
#include<unistd.h>

void commit(){
//--------------------------------------------------------------------------------------------------------------------------
    char filepath[1024];
    char filepath_org[1024];
    char date[128];
    char version_id[128];
    struct stat fileinfo;

    char filename[512];
    char extension[128];
//--------------------------------------------------------------------------------------------------------------------------
    printf("Enter the Filename : ");
    scanf("%s",filepath);
//--------------------------------------------------------------------------------------------------------------------------
    // Getting Current working directory
    char cwd[2048];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {} else {perror("getcwd");}
//--------------------------------------------------------------------------------------------------------------------------
    // Build path to commits directory
    char commits_dir[2048];
    snprintf(commits_dir, sizeof(commits_dir), "%s/../commits", cwd);

    // Check if commits directory exists
    struct stat commits_info;
    if (stat(commits_dir, &commits_info) == 0) {
        // If Directory exists check if it's actually a directory or not
        if (S_ISDIR(commits_info.st_mode)) {
            printf("Commits directory found: %s\n", commits_dir);
        } else { // IF not a directory,... then ask manual intervention 
            printf("Error: 'commits' exists but is not a directory!\nTry to remove the file and retry commit");
            return;
        }
    } else {
        // If  Directory doesn't exist, create it
        printf("Commits directory not found. Creating: %s\n", commits_dir);
        if (mkdir(commits_dir, 0755) == 0) {
            printf("✓ Commits directory created successfully\n");
        } else {
            perror("Failed to create commits directory");
            return;
        }
    }
//--------------------------------------------------------------------------------------------------------------------------
    // Check if entered file is present in the directory
    strcat(cwd,"/");
    strcat(cwd,filepath);
    strcpy(filepath_org,cwd);
    printf("\n %s",cwd);
    if (stat(cwd,&fileinfo)==0){printf("\nFile Present!\n");} else {perror("stat");} 
//--------------------------------------------------------------------------------------------------------------------------
    // Version ID
    strcpy(date,ctime(&(time_t){time(NULL)}));
    strftime(version_id,sizeof(version_id),"%Y%m%d_%H%M%S",localtime(&(time_t){time(NULL)}));
//--------------------------------------------------------------------------------------------------------------------------
    // New Filename
    printf("version id : %s\n",version_id);

    // Look for the last '/' in the path (Unix/Linux/macOS separator)
    const char* basename = strrchr(filepath, '/');

    // If '/' is not found,... then filename is basename
    basename = (basename == NULL) ? filepath : basename + 1;

    // Get the last "." character in the filename
    const char* dot = strrchr(basename, '.');
//--------------------------------------------------------------------------------------------------------------------------
    // Check if Dot is not there or at the start of the file
    // if extension is there as needed
    if (dot != NULL && dot != basename) {
        size_t name_len = dot - basename;
        printf("name_len : %d\n",name_len);

        // To ensure filename storage is large enough
        if (name_len < sizeof(filename)) {
            // Copy filename part everything before the dot excluding it
            strncpy(filename, basename, name_len);
            filename[name_len] = '\0';  // Add null terminator

            // Copy extension part including the dot
            strncpy(extension, dot, sizeof(extension) - 1);
            extension[sizeof(extension) - 1] = '\0';

        } else {
            // Storage is too small so set empty string to indicate error
            filename[0] = '\0';
            printf("Warning: Filename is too long!\n");
        }
    }else{
        // If no extension is there...
        strncpy(filename, basename, sizeof(filename) - 1);
        filename[sizeof(filename) - 1] = '\0';
        extension[0] = '\0';  // Empty extension
    }
    // Extracted Filename and Extension,... now to remove extension and add the version
    char* dot_in_filepath = strrchr(filepath, '.');
    if (dot_in_filepath != NULL) {
        *dot_in_filepath = '\0';  // Replace dot with null terminator
    }
    strcat(filepath,"_");
    strcat(filepath,version_id);
    strcat(filepath,extension);
    printf("Filepath with extension: '%s'\n", filepath);
    printf("Filepath Original: %s\n",filepath_org);
    printf("Commit directory : %s\n",commits_dir);
//--------------------------------------------------------------------------------------------------------------------------
    // COPY FILE and SAVE VERSION INTO COMMITS IS PENDING
    return;
}

int main(){
    printf("Mini Git program is starting !!!\n");
    commit();
    return 0;
}
