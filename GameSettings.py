def confbackup(conf):
  BackupConfigFile = open("GameSettingsDetected.backup", "w")
  BackupConfigFile.write(conf)
  BackupConfigFile.close

true = True
false = False

conf = {
  "FloatingText": {
    "Dodge_Enabled": true,
    "EnemyPhysicalDamage_Enabled": true,
    "Experience_Enabled": false,
    "Gold_Enabled": true,
    "Heal_Enabled": true,
    "Invulnerable_Enabled": true,
    "Level_Enabled": true,
    "ManaDamage_Enabled": false,
    "PhysicalDamage_Enabled": true,
    "QuestReceived_Enabled": true,
    "Score_Enabled": true,
    "Special_Enabled": true
  },
  "General": {
    "AutoAcquireTarget": true,
    "BindSysKeys": false,
    "EnableAudio": true,
    "EnableTargetedAttackMove": true,
    "GameMouseSpeed": 10,
    "HideEyeCandy": false,
    "OSXMouseAcceleration": true,
    "PredictMovement": false,
    "RelativeTeamColors": false,
    "ShowCursorLocator": false,
    "ShowGodray": true,
    "ShowTurretRangeIndicators": true,
    "SnapCameraOnRespawn": false,
    "ThemeMusic": 0,
    "WaitForVerticalSync": true,
    "WindowMode": true
  },
  "HUD": {
    "AutoDisplayTarget": true,
    "CameraLockMode": 1,
    "ChatScale": 21,
    "DisableHudSpellClick": false,
    "DrawHealthBars": true,
    "EnableLineMissileVis": false,
    "FlashScreenWhenDamaged": false,
    "FlashScreenWhenStunned": false,
    "FlipMiniMap": false,
    "GlobalScale": 0.05000000074505806,
    "KeyboardScrollSpeed": 0.07999999821186066,
    "MapScrollSpeed": 0.10000000149011612,
    "MiddleClickDragScrollEnabled": false,
    "MinimapMoveSelf": true,
    "MinimapScale": 0.5,
    "MirroredScoreboard": false,
    "NumericCooldownFormat": 1,
    "ObjectTooltips": true,
    "ScrollSmoothingEnabled": false,
    "ShowAllChannelChat": true,
    "ShowAttackRadius": false,
    "ShowNeutralCamps": true,
    "ShowSpellCosts": false,
    "ShowSummonerNames": true,
    "ShowSummonerNamesInScoreboard": false,
    "ShowTeamFramesOnLeft": false,
    "ShowTimestamps": true,
    "SmartCastOnKeyRelease": false,
    "SmartCastWithIndicator_CastWhenNewSpellSelected": false
  },
  "LossOfControl": {
    "LossOfControlEnabled": true,
    "ShowSlows": false
  },
  "Performance": {
    "EnableHUDAnimations": true
  },
  "Voice": {
    "ShowVoiceChatHalos": false,
    "ShowVoicePanelWithScoreboard": false
  },
  "Volume": {
    "AmbienceMute": false,
    "AmbienceVolume": 0.44999998807907104,
    "AnnouncerMute": false,
    "AnnouncerVolume": 0.15000000596046448,
    "MasterMute": false,
    "MasterVolume": 0.20000000298023224,
    "MusicMute": false,
    "MusicVolume": 0.0,
    "PingsMute": false,
    "PingsVolume": 0.30000001192092896,
    "SfxMute": false,
    "SfxVolume": 0.4000000059604645,
    "VoiceMute": false,
    "VoiceVolume": 0.4000000059604645
  }
}