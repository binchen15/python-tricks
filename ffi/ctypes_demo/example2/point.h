typedef struct {
    int x;
    int y;
} Point;

void show_point(Point point);
void move_point(Point point);
void move_point_by_ref(Point *point);
Point get_point(void);
