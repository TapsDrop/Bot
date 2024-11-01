<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Promo Code Generator</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="shortcut icon" href="favicon.png" type="image/x-icon">
</head>
<body>
    <div class="container">
        <h1>Game Promo Code Generator</h1>
        <div class="form-group">
            <label for="gameSelect">Select Game</label>
            <select id="gameSelect">
                <option value="1">ZooPolis </option>
                <option value="2">Coming Soon...</option>
                <option value="3">Snake Run(new)</option>
                <option value="4">Train Miner</option>
                <option value="5">Merge Away </option>
                <option value="6">Cooking Stories (new)</option>
                <option value="7">Polysphere</option>
                <option value="8">Snake Run</option>
                <option value="9">Factory World </option>
                <option value="10">Stone Age </option>
                <option value="11">Bouncemasters </option>
                <option value="12">Hide Ball </option>
                <option value="13">Infected Frontier </option>
                <option value="14">Count Masters</option>
            
                
                

            </select>
        </div>

        <div id="google_translate_element"></div>
        <script type="text/javascript">
            function googleTranslateElementInit() {
                new google.translate.TranslateElement({
                    pageLanguage: 'en', 
                    includedLanguages: 'en,hi,ta,ru,id,ha,pt', 
                    layout: google.translate.TranslateElement.InlineLayout.SIMPLE
                }, 'google_translate_element');
            }
            
        </script>
        <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
        

        
        <div class="form-group">
            <label id="keyCountLabel" for="keyCountSelect">Number of keys:</label>
            <select id="keyCountSelect">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="8">8</option>
                
            </select>
        </div>
        <button id="startBtn">Generate Keys</button>
        
        <div id="progressContainer" class="hidden">
            <div class="progress-bar">
                <div id="progressBar"></div>
            </div>
            <div id="progressText">0%</div>
            <div id="progressLog">Starting...</div>
            <div id="countdownContainer">
            <p>Next Step will start in: <span id="countdownTimer"></span> seconds </p>
            </div>
        </div>
        <div id="keyContainer" class="hidden">
            <h3 id="generatedKeysTitle" class="hidden">Generated Keys:</h3>
            <div id="keysList"></div>
            <button id="copyAllBtn" class="hidden">Copy All Keys</button>
            <div id="copyStatus" class="hidden">Copied!</div>
            <!-- <button id="generateMoreBtn">Generate More Keys</button> -->
        </div>


        <label>
            <input type="checkbox" id="logCheckbox"> Enable Logs
        </label>
        <textarea id="logArea" rows="3" readonly style="width: 100%; resize: none; font-size: 12px; display: none;"></textarea>

        <div class="mycodes">
            <p>
                The Key Generation may take upto 10 mins<br>
                Wanna Earn More on Crypto AirDrop for FREE 👉<a href="https://t.me/Insta_Buy_Follower/136">Join Verified Bot 🔜 </a>
            </p>
            <button id="ShowKeysBtn">My Codes</button>
            <div id="generatedCodesContainer" style="display:none;">
                <h3>Today's Generated Codes:</h3>
                <ul id="generatedCodesList"></ul>
            </div>

        </div>
        <div class="footer">
            <p>Disclaimer: This tool is for educational purposes only. Use responsibly.
                Any Issues in the Key Generation 👉<a href="https://t.me/Insta_Buy_Follower/118"> Check FAQ'S </a>
            <button id="telegramChannelBtn">Check out Our Telegram Channel 🆔</button></p>
            <button id="creatorChannelBtn">Contact Creator 🤖</button> 
            
        </div>
    </div>
    <script src="script.js"></script>
</body>

</html>
