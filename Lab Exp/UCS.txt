START

Input Graph, Start Node and Goal Node

Create a Priority Queue
Insert Start Node with Cost = 0

WHILE Priority Queue is not empty DO

    Remove node with minimum cost

    IF node is Goal THEN
        Print Cost
        STOP
    END IF

    IF node is not visited THEN
        Mark node as visited

        FOR each adjacent node DO
            New Cost = Current Cost + Edge Cost
            Insert adjacent node with New Cost
        END FOR
    END IF

END WHILE

STOP
