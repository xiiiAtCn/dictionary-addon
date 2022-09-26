Dictionary = LibStub("AceAddon-3.0"):NewAddon("Dictionary", "AceConsole-3.0", "AceEvent-3.0")

function Dictionary:OnInitialize()
-- Called when the addon is loaded
  self:Print("Hello World!")
-- register chat commands
  self:RegisterChatCommand("dic", "SlashCommand")
  self:RegisterChatCommand("dictionary", "SlashCommand")
end

function Dictionary:OnEnable()
-- Called when the addon is enabled
  self:RegisterEvent("ZONE_CHANGED")
end

function Dictionary:OnDisable()
  -- Called when the addon is disabled
end

function Dictionary:ZONE_CHANGED()
  local subzone = GetSubZoneText()
  self:Print("Current Place", subzone)
  self:Print("You have changed zones!", GetZoneText(), subzone)
  if GetBindLocation() == subzone then
    self:Print("Welcome Home!")
  end
end

function Dictionary:SlashCommand(msg) 
  if msg == "ping" then
    self:Print("pong")
  else
    self:Print("hello there: ", msg)
  end
end
