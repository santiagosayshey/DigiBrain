![](https://lh6.googleusercontent.com/JdUM4yrCDunUIrcJlOlBCVMFXGs4aKI_iiTUaSH5LVmnmLrxEsqr-UalWf1ZSI9PxC7dpc3UE7ZHWdblHwvHoao7ts7d5TlyGUZpf_E0o4ncQRdRfhPS6rItaZvpreaRb-9iCTwPg7oCu540SARXThI)

## Project Idea:

Turn Based Rogue-Like presented entirely using OOP and SFML. Rogue-Likes are video games based on the game ‘Rogue’, originally released in 1980 and are usually characterised by perma-death and randomly generated dungeons. Popular examples include Slay the Spire, The Binding of Isaac, Faster than Light and Hades. 

```
Rogue-like is a catch all term that spans a variety of games over the past 40 years and really can be anything. It’s an interface for video games! They all have the same ‘gameplay loop’ at heart but often evolve into something much more unique. This is what makes it the perfect candidate for a coding project.
```

![](https://lh4.googleusercontent.com/dLKNWOIgrecnC-m2gX2ob7C_kL3sRN8G6YY0vuPPYKglX-BiODk5EJLDqFYDTqzEa0SBnUb2bRWEnuz2aPS85o81r6eAmtC-aMQuTLhIYTYNRfrCjEEZLcMmNv40qR39urUnlIqDrPg9_vBpfgmi6uw)

[https://github.com/santiagosayshey/OOProject](https://github.com/santiagosayshey/OOProject)

## Use Cases / Interactions & User Interface:

### General Idea: 

Each game will always consist of two components - the current game state and the player. Once a new game instance is created, a window will launch, which can be used by the player to interact with the game. The game will work by updating and drawing  ‘drawables’ inside the window each frame. These drawables consist of textures, animated sprites, text and buttons. Each of these drawables will be able to check for collisions as well as update and draw themselves in the current state. The game state defines what entities will be updated and drawn every frame and therefore allow the game to dynamically change its behaviour based on user input. This is achieved by allowing the game to set its own state, and allowing each state to have different definitions of how it updates and renders the current window, whereby each definition can override every other definition. 

*This idea generalises the entirety of the game, which is further expanded upon in the next section where more concrete objects and behaviours are identified and explored.* 

  

### Specific Ideas: 

Building upon this general idea, we can clearly identify some interfaces that will derive a number of different objects that allow the game to scale linearly. This section will cover a majority of the different scenarios in which these inherited classes may operate. It will also heavily cover the interactivity and user interface portion of this plan. 

- Splash Screen

The game begins by loading into the splash state, where a texture is loaded in and used as the background. This texture is used to display the title. The player can advance into the next state by pressing a key on their keyboard. This is achieved by using an event manager, which checks for key presses when the current state updates.  The same is used for mouse clicks and other SFML events such as closing the window. 

- Main Menu
The game will then change into the menu state, which consists of 2 buttons - play and quit. Hovering over each button will update the colour of the button, indicating to the player that they are able to click it. Clicking the button results in the game changing its state; Clicking the quit button will close the window and end the game. Clicking the play button will change the game into the character select state. The menu state also includes another texture similar to the splash screen. 

- Character Select
Within the character select state, the player is able to choose a character to play with. 3 buttons corresponding to three different characters will be displayed, and when clicked, will change the displayed character. The character’s sprite will play an idle animation in the window. This is achieved through the event manager. More information on animation can be found in the function explanations. The button will also draw a text drawable, describing the stats of each of the characters. This button also updates the player’s stats corresponding to each of the characters. These stats include health, armour, attack power, strengths, weaknesses, accuracy, evasion, experience and current level. Once the player has made their decision, they can click the embark button, which will save the current stats to the player and switch the game state to gameplay. 

- Gameplay
The gameplay state derives into various states. This means that each of the states may coexist, and that their information is not destroyed and can therefore be used amongst each other.

- Map
The map state: In this state, a map texture will be displayed and static sprites will be randomly generated in each of the empty level slots. These sprites represent the different levels that the player must beat to win the game. The game consists of dynamic progression, in which the player chooses their own path to the boss. These levels include enemy encounters, treasure rooms, and mystery rooms. To pick a level, the player must have beaten the previous level, and click a current level. Clicking a level results in a new game state:

- Enemy Encounter
This section is planned to be developed using agile methodology and is subject to major changes. The following tries to briefly capture the essence of what these encounters are meant to be. They do not represent the final result. Enemy encounters will use each of the drawables and have multiple inherited gameplay states. 

This section involves using turn based combat to simulate a fight between the player and the enemy. The player and enemy will take turns performing actions on each other such as attacking and defending. These actions may impact their stats and lead to various different states. Attacking the enemy may result in them losing all their health and dying. Similar results can happen to the player. The different scenarios that can occur during an enemy encounter are as follows: Fight start, Player turn, Enemy turn, Player wins, Enemy wins. More could be added in the future. There will also be drawables such as text and buttons to dynamically update the stats of the player and display them on screen. This includes scenarios in which the player is damaged and their health text will update on screen to reflect this. Moreover, sound effects will also be used for greater spectacle. If the player beats a non boss enemy, they will return to the map and select a new level. If they die, they will be sent to the main menu and flavour game over text will display on the screen. 

- Treasure Level
In the treasure state, the player’s current experience is increased such that it results in a level up. When the player levels up, they can choose to increase one of their stats - health, attack power, accuracy or evasion. These are represented with buttons. There also should be a treasure texture loaded in as the background. Once the player has made their choice, the game switches back to the map state. 

- Mystery Level
The mystery state randomly picks between the treasure state and the enemy encounter state. 

In the case that the player beats all the levels, this means they have beaten the entire game, resulting in a game victory state. This state removes all previous states and displays text explaining to the player they have won. It will show stats such as run time, high score, etc. The game will then switch back to the menu state where the player can start a new game or quit.

*Now that we have thoroughly identified any potential objects and their data members / behaviours, it is vital to create a UML class diagram which will not only contain this information, but also highlight any aggregation and hierarchical relationships.*

## UML Class Diagram

![[docs/Images/UML Class Diagram.drawio 1.png]]

## Functions

The previous UML diagram has provided a concise foundation that will be heavily utilised in the development of this project. While important in showcasing the grand picture, it still leaves vital information out regarding how any of it actually works. This section aims to explain how the important ideas of this project are encapsulated in code.
### Game Loop and State Pattern

The most important coding idea of this project is the ‘game loop’. The game loop is the overall flow control for the entire game program. It's a loop because the game keeps doing a series of actions repeatedly until the user quits. In this particular game, we define the game loop as a while loop that iterates as long as the window is open. In the game object, this behaviour is called the run function.

The second most important coding idea of this project is the ‘state pattern’. The state pattern is a behavioural design pattern that allows an object, in this case, the game; to change its behaviour based on its state. We assign a current state to the game, and allow that state to control the while loop. We achieve this by creating a ‘state’ interface that is declared within the game instance and controls the update and render functions in the game loop. We use polymorphism within the derived state classes to override the parent update and render functions and therefore allow the game to dynamically update and render based on its current state. The game instance is also able to update its own current state. We also allow the current state to change itself by passing the current game instance into the new state. The game state is passing itself to the next game. An issue of circular dependency arises with this however, and so the state interface must forward declare the game class instead of including it.

```cpp
Game::Game(int width, int height)
{
    player = new Player;
    this->window = new sf::RenderWindow(sf::VideoMode(width,height),"Test");
    this->currentState = new PickState(this, player);
}


void Game::run()
{
    while (window->isOpen())
    {
        this->currentState->update(window);
        this->currentState->render(window);
    }
}


void Game::setState(State* newState)
{
    currentState = newState;
}
```
### Update()

Event manager, state updating. Update any drawables currently in the frame. Check for button clicks, mouse presses and key clicks. Event manager is needed so that events occur once in the game.

```cpp
void PlayState::update(sf::RenderWindow* window)
{
    wiz->update(window);
    wizhealth->update(window);
    while (window->pollEvent(event))
    {
        // "close requested" event: we close the window
        switch (event.type) {
            case sf::Event::Closed: {
                window->close();
                break;
            }
            case sf::Event::MouseButtonReleased: {
                if (attack->checkCollision(window)) {
                    player->attack(enemy);
                    break;
                }
                if (attackP->checkCollision(window)) {
                    enemy->attack(player);
                    break;
                }
            }
            case sf::Event::KeyReleased: {
                    break;
            }
        }
    }
}
```

### Render()

Clear the previous frame, render the updated drawables and display them.

```cpp
    window   ->clear(sf::Color::White);
    wiz->draw(window);
    wizhealth->draw(window);
    attack->draw(window);
    attackP->draw(window);
    enemy->draw(window);
    player->draw(window);
    healthShadow->draw(window);
    health->draw(window);
    window   ->display();
```

## Drawables

Now that we can adequately control the flow of the game, we can begin populating each stage. This is achieved using ‘drawables’. Drawables are things that appear on the screen during gameplay. They are capable of drawing and updating themselves as well as checking if they are colliding with another drawable. In more advanced cases, they are also capable of animating themselves.

### Sprite Class

```cpp
Sprite::Sprite(std::string texture, int x, int y, int size, int scale)
{
    this->size = size;
    this->texture = new sf::Texture;
    this->texture->loadFromFile(texture);
    this->texture->setRepeated(true);
    sprite = new sf::Sprite;
    sprite->setTexture(*(this->texture));
    sprite->setTextureRect(sf::IntRect(0, 0, size, size));
    sprite->setScale(scale, scale);
    sprite->setOrigin(size / 2, size / 2);
    sprite->setPosition(x, y);
    currentFrame = 0;
    numFrames = 7;
    row = 0;
}
```

### checkCollision()

Return a boolean of whether the bounds of a drawable contains the bounds of another drawable. Can also be configured to work with the mouse bounds for button presses.

```cpp
bool Button::checkCollision(sf::RenderWindow* window)
{
    sf::Vector2f mouse = window->mapPixelToCoords(sf::Mouse::getPosition(*window));
    sf::FloatRect bounds = text.getGlobalBounds();
    return bounds.contains(mouse);
}
```

### updateAnimation()

Pass the current row and number of frames so that the animation function can switch to that.

```cpp
void Sprite::updateAnimation(int numFrames, int row)
{
    currentFrame = 0;
    this->numFrames = numFrames;
    this->row = row;
}
```
### animation()

When a behaviour prompts a drawable to animate itself, the current state’s event manager will tell the drawable to update its sprite’s texture rectangle. A texture rectangle is a defined rectangle located within a sprite sheet. These rectangles can be categorised as ‘frames’ of an animation and can therefore be iterated through to simulate movement. The type of animation being played is dependent on the number of frames in an animation and its row location in the sprite sheet. This row is iterated in real time, specifically every 0.1 seconds to detach the speed of the movement from the frame rate. This is important because we want some behaviours to work as fast as possible but others to work in a set time, as is the case for animation. Animation is called every update, regardless of if it is updated or not and always defaults to playing an ‘idle’ animation.

```cpp
bool Sprite::animation(bool repeat)
{
    if (clock.getElapsedTime().asSeconds() > 0.1f)
   
    {
        clock.restart();
        if (currentFrame != numFrames)
        {
            if (currentFrame > 8)
            {
                sprite->setTextureRect(sf::IntRect(size * currentFrame, size * row + size, size, size));
                currentFrame++;
            }
            else
            {
                sprite->setTextureRect(sf::IntRect(size * currentFrame, size * row, size, size));
                currentFrame++;
            }
        }
        else
        {
            if (repeat == true)
            {
                // set current frame to 0 IF the animation needs to be repeated
                currentFrame=0;
            }
            else
                // if not repeated, play idle animation
                updateAnimation(7, 0);
                return true;
        }
    }
    return false;
}
```

## Time Plan

Now that the general core idea of the project has been identified and some proof of concept coding has been completed, it is vital that a proper time plan be created to ensure success in the development portion of this project. The table below provides our general outline for the planning, development, and delivery of the project. As stages are being planned pre-emptively, they are susceptible to change and we may not strictly adhere to it.

![](https://lh5.googleusercontent.com/ZBHzOv5W2jpMY7MiUNt-M86DTvmD4dx3cKcLWTapTXd4-r5ISJrdSM3G9-RTEhhQGXIq9NKqnEjz9xQb7j_zHivcWzo1haOB2330jq5nIuHmYr31w4ohR94vSCg0OMl1JUn2C4FqqOWMvv1o1ECQhBg)


## Unit Testing and Debugging

To ensure that each component of the program works harmoniously, it is vital that they first work individually. This will be ensured through the  processes of unit testing and debugging, performed incrementally throughout development. 

This will be achieved through the encapsulation of different objects and writing driver programs to assess their functionality. While writing programs, there are several processes to be done to make the process of debugging easier. These include: Commenting to explain functionality and writing  test cases and evaluating their output

Such information will be compiled in a kanban board and include the following:

- Brief summary of their functionality, such that other members could understand the purpose of individual functions or classes and assist in debugging
- Different test cases that identify areas that encompass the possibility of significant problems and challenges
- Expected output / actual output. Given that each of the individual group members will be assigned different parts of the program, unit testing can be conducted locally within a member’s personal computer before merging with the collaborative program. 

Throughout the process of writing the program, numerous errors and issues may arise that extend the time required for completion. Therefore, the process of debugging is vital for prompt elimination of such errors and issues. By adhering to the structure stated in the process of testing; implementing comments, writing test cases, and evaluating expected outputs against actual outputs, problems identified through test cases can be traced to their sources much easier, thus making debugging much simpler. When sources of the bugs are identified, debugging can occur as such:

1. Reproduce the bug
2. Isolating the code in which errors are identified
3. Capture snapshot of the program at its current state; when the bug appears (output all variable values and states of the program)
4. Analyse the snapshot to find cause of the bug
5. Fix the bug, and continue with test cases to ensure that no new bugs appear

In order to take an iterative approach and make our development modular, we are also employing the use of a “Kanban” board that is connected to GitHub. This allows us to assign tasks to specific group members, and clearly display their progress (in the “Backlog”, “In Progress”, and “Completed”). This will help in the reduction of merge conflicts, as group members know the exact section they are supposed to be working on. A screenshot of the board is displayed below:

![](https://lh5.googleusercontent.com/k9Mj5shQyJunyxvFHThs3O-LuqznD88RQNUZ9U4aI7KxMpqrZ90-cgMTmi79MaWx_exZKVZENZn08xv5-ULj072RtpgWg7qUJAJyp_Ab5Yz_wyWIl8ZmYI5HJNoBR1-yjYVIuRECj5yLQnNzO2cgLfc)
