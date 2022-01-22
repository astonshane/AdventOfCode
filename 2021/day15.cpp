#include <iostream>
#include <queue>
#include <fstream>
#include <vector>
#include <tuple>

class Node {
    public:
        int x;
        int y;
        int dist;
        bool visited;
        Node(int a, int b): x(a), y(b), dist(INT_MAX), visited(false) {}
};

struct CustomCompare
{
    bool operator()(const Node* lhs, const Node* rhs)
    {
        return lhs->dist > rhs->dist;
    }
};

using namespace std;

int execute(vector<vector<int> >& risks, vector<vector<Node*> >& nodes, vector<Node*>& pq) {
    int goal_y = nodes.size() - 1;
    int goal_x = nodes[0].size() - 1;

    nodes[0][0]->dist = 0;

    vector<tuple<int,int> > neighbors;
    neighbors.push_back(std::make_tuple(-1,0));
    neighbors.push_back(std::make_tuple(1,0));
    neighbors.push_back(std::make_tuple(0,-1));
    neighbors.push_back(std::make_tuple(0,1));

    while (pq.size() > 0)
    {
        // slow as hell... need a better solution for the priority queue than a vector that gets sorted each loop iteration
        sort(pq.begin(), pq.end(), CustomCompare());
        Node* n = pq.back();
        n->visited = true;
        pq.pop_back();
        //cout << n->x << " " << n->y << " " << n->dist << std::endl;

        if (n->x == goal_x && n->y == goal_y) {
            return n->dist;
        }

        for (auto& t: neighbors) {
            int new_x = n->x + get<0>(t);
            int new_y = n->y + get<1>(t);
            if (new_y >= 0 && new_y < nodes.size() && new_x >= 0 && new_x < nodes[0].size()) {
                Node* n2 = nodes[new_y][new_x];
                if (n2->visited) {
                    continue;
                }
                int new_dist = n->dist + risks[new_y][new_x];
                if (new_dist < n2->dist) {
                    n2->dist = new_dist;
                }
            }
        }

    }
    return -1;
}

void part1() {
    vector<Node*> pq;
    vector<vector<int> > risks;
    vector<vector<Node*> > nodes;


    ifstream infile("inputs/day15.txt");
    string line;
    int y=0;
    while (getline(infile, line)) {
        vector<int> risks_row;
        vector<Node*> nodes_row;
        
        for (int i=0; i<line.size(); i++) {
            int risk = (int)line[i] - 48;
            risks_row.push_back(risk);

            Node* n = new Node(i, y);
            nodes_row.push_back(n);
            pq.push_back(n);

        }
        risks.push_back(risks_row);
        nodes.push_back(nodes_row);
        y += 1;
    }

    cout << "part1: " << execute(risks, nodes, pq) << endl;
}

void part2() {
    vector<Node*> pq;
    vector<vector<int> > base_risks;
    vector<vector<int> > risks;
    vector<vector<Node*> > nodes;


    ifstream infile("inputs/day15.txt");
    string line;
    while (getline(infile, line)) {
        vector<int> risks_row;
        
        for (int i=0; i<line.size(); i++) {
            int risk = (int)line[i] - 48;
            risks_row.push_back(risk);
        }
        base_risks.push_back(risks_row);
    }

    int real_depth = base_risks.size();
    int true_depth = base_risks.size() * 5;
    int real_width = base_risks[0].size();
    int true_width = base_risks[0].size() * 5;

    for (int y=0; y<true_depth; y++) {
        vector<Node*> node_row;
        vector<int> risks_row;
        for (int x=0; x<true_width; x++) {
            Node* n = new Node(x, y);
            node_row.push_back(n);
            pq.push_back(n);

            int base_risk = base_risks[y % real_depth][x % real_width];
            int modifier = int(x / real_width) + int(y / real_depth);

            int risk = base_risk + modifier;
            if (risk > 9) {
                risk = risk % 10 + 1;
            }
            //cout << x << "," << y <<" " << risk << endl;
            risks_row.push_back(risk);
        }
        nodes.push_back(node_row);
        risks.push_back(risks_row);
    }

    /*for (int i=0; i<risks.size(); i++) {
        for (int j=0; j<risks.size(); j++) {
            cout << risks[i][j];
        }
        cout << endl;
    }*/

    cout << "part2: " << execute(risks, nodes, pq) << endl;
}

int main() {
    part1();
    part2(); // slow, but it works
}