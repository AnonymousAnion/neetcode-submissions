class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:

            #print("Asteroid: ", asteroid)

            if not stack:

                stack.append(asteroid)
                continue
            
            if asteroid > 0:

                stack.append(asteroid)
                
                # if stack[-1] > 0:

                #     stack.append(asteroid)

                # else: # Asteroid positive, stack negative

                #     # Collison
                #     if abs(stack[-1]) < asteroid:

                #         while stack and abs(stack[-1]) < asteroid:

                #             stack.pop()

                #         # Only add the asteroid if it destroys
                #         # all asteroids that were in the stack
                #         if not stack:

                #             stack.append(asteroid)

                #     elif abs(stack[-1]) == asteroid:

                #         stack.pop() # Both destroyed

            else:
                
                if stack[-1] < 0:

                    stack.append(asteroid)

                else: # Asteroid Negative, stack positive

                    while stack and stack[-1] > 0 and abs(asteroid) > stack[-1]:

                        stack.pop()

                    # Only add the asteroid if it destroys
                    # all asteroids that were in the stack
                    if not stack or stack[-1] < 0:

                        stack.append(asteroid)

                    if stack[-1] == abs(asteroid):

                        stack.pop() # Both destroyed

            #print(stack)
        
        return stack