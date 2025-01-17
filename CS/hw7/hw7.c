#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
typedef struct {
   int count;
   int pending_posts;
   pthread_mutex_t mut;
 } sem_t;

sem_t sem_prod, sem_cons;
int buffer[4];
int first_occupied_slot = 0;
int first_empty_slot = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;



void sem_init(sem_t *sem, int pshared, unsigned int value) {

   sem->count = value; // 
   pthread_mutex_init(&sem->mut, NULL);
   sem->pending_posts = value; 
 }

void sem_post(sem_t *sem) {
    pthread_mutex_lock(&sem->mut);
    sem->count++;
    sem->pending_posts++;
    pthread_mutex_unlock(&sem->mut);
}
void sem_wait(sem_t *sem) {
    pthread_mutex_lock(&sem->mut);
    sem_t mysem = *sem;  
    sem->count--;
    //int done = 0;
    if (sem->count < 0) {
        sleep:
        pthread_mutex_unlock(&sem->mut);

        while (sem->pending_posts <= 0) {
        }
        pthread_mutex_lock(&sem->mut);
    }
    if (sem->pending_posts > 0)
      sem->pending_posts--;
    else
      goto sleep;
    pthread_mutex_unlock(&sem->mut);
}




// put
void add(int val) {
  buffer[first_empty_slot] = val;
  first_empty_slot++;
  if (first_empty_slot >= 4)
    first_empty_slot = 0;
}
//get
int rem() {
  int val = buffer[first_occupied_slot];
  first_occupied_slot++;
  if (first_occupied_slot >= 4)
    first_occupied_slot = 0;
  return val;
}


void *consumer(void *arg) {
  while (1) {
    sleep(rand() % 5);
    sem_wait(&sem_cons); 
    pthread_mutex_lock(&mutex);
    int tmp = rem();
    printf("%d\n", tmp);
    pthread_mutex_unlock(&mutex);
    sem_post(&sem_prod);
  }
}

void *producer(void *arg) {
  int item = 1;
  while (1) {
    sleep(rand() % 5);
    sem_wait(&sem_prod); 
    pthread_mutex_lock(&mutex);
    add(item++);
    pthread_mutex_unlock(&mutex);
    sem_post(&sem_cons);
  }
}



int main(int argc, char *argv[]) {
  //printf("IM IN MAIN");
  //fflush(stdout);

  sem_init(&sem_cons, 0, 0);
  sem_init(&sem_prod, 0, 4);
  int i;
  int j;
  //printf("sem_init done");
  //fflush(stdout);

  pthread_t thread_prod[3], thread_cons[3];
  for (i = 0; i < 3; i++){
    pthread_create(&thread_prod[i], NULL, producer, NULL);
    pthread_create(&thread_cons[i], NULL, consumer, NULL);
  }
  //printf("threads created done");
  //fflush(stdout);
  for (j = 0; j < 3; j++){
    pthread_join(thread_prod[j], NULL);
    pthread_join(thread_cons[j], NULL);
  }
  //printf("threads join done");
  //fflush(stdout);

}
