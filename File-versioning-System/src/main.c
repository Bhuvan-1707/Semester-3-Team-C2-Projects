#include<time.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/stat.h>

// Struct Metadata of a file for containing all the commit information
struct Metadata{
    char filename[256];
    char rel_filepath[512];
    char version_id[64];
    long size;
    char date[64];
};

// Create Metadata - (create a file function)
void create_metadata(char* filename, struct Metadata metadata){
    // Copy Filename string from the function input to the structure metadata
    strcpy(metadata.filename,filename);
    // Copy the relative file path from the present working directory
    char cwd[1024];
    if(getcwd(cwd,sizeof(cwd))!=NULL){
        // TODO
    }
    // Copy the time taken from time() converted to string by ctime()
    strcpy(metadata.date,ctime(&(time_t){time(NULL)}));
    // Take the time(), make it into localtime(), use metadata.version_id as buffer to convert the localtime into timestamp - version id
    strftime(metadata.version_id,sizeof(metadata.version_id),"%Y%m%d_%H%M%S",localtime(&(time_t){time(NULL)}));
    // Size finder and adds it into metadata
}

// Log writer function
// TODO

void main(){
    printf("Mini Git Program starts execution !!!\n");

    return;
}
