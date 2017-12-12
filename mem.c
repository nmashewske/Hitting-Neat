#include <sys/uio.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
float health2(pid_t pid)
{
    struct iovec local[2];
    struct iovec remote[1];
    char buf1[4] = {'a', 'b', 'c', 'd'};
    
    local[0].iov_base = buf1;
    local[0].iov_len = 4;
    remote[0].iov_base = (void *) 0xc32360;
    remote[0].iov_len = 4;
    process_vm_readv(pid, local, 1, remote, 1, 0);
    float f;
    memcpy(&f, buf1, 4);
    return(f);
}
float health1(pid_t pid)
{
    struct iovec local[2];
    struct iovec remote[1];
    char buf1[4] = {'a', 'b', 'c', 'd'};
    
    local[0].iov_base = buf1;
    local[0].iov_len = 4;
    remote[0].iov_base = (void *) 0xc32350;
    remote[0].iov_len = 4;
    process_vm_readv(pid, local, 1, remote, 1, 0);
    float f;
    memcpy(&f, buf1, 4);
    return(f);
}
int comboStage1(pid_t pid)
{
    struct iovec local[2];
    struct iovec remote[1];
    char buf1[4] = {'a', 'b', 'c', 'd'};
    
    local[0].iov_base = buf1;
    local[0].iov_len = 4;
    remote[0].iov_base = (void *) 0xc32300;
    remote[0].iov_len = 4;
    process_vm_readv(pid, local, 1, remote, 1, 0);
    int i;
    memcpy(&i, buf1, 4);
    return(i);
}
float comboDamage1(pid_t pid)
{
    struct iovec local[2];
    struct iovec remote[1];
    char buf1[4] = {'a', 'b', 'c', 'd'};
    
    local[0].iov_base = buf1;
    local[0].iov_len = 4;
    remote[0].iov_base = (void *) 0xc322f8;
    remote[0].iov_len = 4;
    process_vm_readv(pid, local, 1, remote, 1, 0);
    float f;
    memcpy(&f, buf1, 4);
    return(f);
}
