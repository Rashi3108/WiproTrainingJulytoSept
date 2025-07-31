#!/usr/bin/env python3
"""
Downloads Folder Organizer
A cross-platform Python script to organize files in the Downloads folder
by categorizing them into subfolders based on file types.

Compatible with: Windows, macOS, and Linux
Author: DevOps Automation Script
"""

import os
import shutil
import platform
from pathlib import Path
from datetime import datetime
import logging

class DownloadsOrganizer:
    def __init__(self):
        self.system = platform.system()
        self.downloads_path = self.get_downloads_path()
        self.setup_logging()
        
        # File type categories
        self.file_categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages'],
            'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
            'Presentations': ['.ppt', '.pptx', '.odp', '.key'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
            'Executables': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm', '.appimage'],
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'],
            'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
            'eBooks': ['.epub', '.mobi', '.azw', '.azw3', '.fb2'],
            'CAD': ['.dwg', '.dxf', '.step', '.iges', '.stl'],
            'Others': []  # Fallback category
        }
    
    def get_downloads_path(self):
        """Get the Downloads folder path based on the operating system"""
        if self.system == "Windows":
            # Windows Downloads folder
            return Path.home() / "Downloads"
        elif self.system == "Darwin":  # macOS
            # macOS Downloads folder
            return Path.home() / "Downloads"
        else:  # Linux and other Unix-like systems
            # Linux Downloads folder
            return Path.home() / "Downloads"
    
    def setup_logging(self):
        """Setup logging configuration"""
        log_file = self.downloads_path / "organizer.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def get_file_category(self, file_extension):
        """Determine the category of a file based on its extension"""
        file_extension = file_extension.lower()
        
        for category, extensions in self.file_categories.items():
            if file_extension in extensions:
                return category
        
        return 'Others'
    
    def create_category_folders(self):
        """Create category folders if they don't exist"""
        created_folders = []
        
        for category in self.file_categories.keys():
            if category != 'Others':  # We'll create Others folder only if needed
                folder_path = self.downloads_path / category
                if not folder_path.exists():
                    folder_path.mkdir(exist_ok=True)
                    created_folders.append(category)
                    self.logger.info(f"Created folder: {category}")
        
        return created_folders
    
    def move_file(self, source_path, destination_folder):
        """Safely move a file to the destination folder"""
        try:
            destination_path = self.downloads_path / destination_folder
            
            # Create destination folder if it doesn't exist
            destination_path.mkdir(exist_ok=True)
            
            # Handle file name conflicts
            destination_file = destination_path / source_path.name
            counter = 1
            
            while destination_file.exists():
                name_parts = source_path.stem, counter, source_path.suffix
                new_name = f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                destination_file = destination_path / new_name
                counter += 1
            
            # Move the file
            shutil.move(str(source_path), str(destination_file))
            self.logger.info(f"Moved: {source_path.name} → {destination_folder}/")
            return True
            
        except Exception as e:
            self.logger.error(f"Error moving {source_path.name}: {str(e)}")
            return False
    
    def organize_downloads(self, dry_run=False):
        """Main function to organize the downloads folder"""
        if not self.downloads_path.exists():
            self.logger.error(f"Downloads folder not found: {self.downloads_path}")
            return False
        
        self.logger.info(f"Starting organization of: {self.downloads_path}")
        self.logger.info(f"Operating System: {self.system}")
        
        if dry_run:
            self.logger.info("DRY RUN MODE - No files will be moved")
        
        # Get all files in downloads folder (excluding subdirectories)
        files_to_organize = [f for f in self.downloads_path.iterdir() 
                           if f.is_file() and not f.name.startswith('.')]
        
        if not files_to_organize:
            self.logger.info("No files found to organize")
            return True
        
        # Create category folders
        if not dry_run:
            self.create_category_folders()
        
        # Statistics
        stats = {category: 0 for category in self.file_categories.keys()}
        moved_files = 0
        failed_files = 0
        
        # Process each file
        for file_path in files_to_organize:
            file_extension = file_path.suffix
            category = self.get_file_category(file_extension)
            
            stats[category] += 1
            
            if dry_run:
                self.logger.info(f"Would move: {file_path.name} → {category}/")
            else:
                if self.move_file(file_path, category):
                    moved_files += 1
                else:
                    failed_files += 1
        
        # Print summary
        self.print_summary(stats, moved_files, failed_files, dry_run)
        return True
    
    def print_summary(self, stats, moved_files, failed_files, dry_run):
        """Print organization summary"""
        print("\n" + "="*50)
        print("📁 DOWNLOADS ORGANIZATION SUMMARY")
        print("="*50)
        
        action = "Would be organized" if dry_run else "Organized"
        
        for category, count in stats.items():
            if count > 0:
                print(f"📂 {category}: {count} files")
        
        print("-"*50)
        if not dry_run:
            print(f"✅ Successfully moved: {moved_files} files")
            if failed_files > 0:
                print(f"❌ Failed to move: {failed_files} files")
        else:
            total_files = sum(stats.values())
            print(f"📊 Total files to organize: {total_files}")
        
        print(f"📍 Location: {self.downloads_path}")
        print(f"🖥️  System: {self.system}")
        print("="*50)
    
    def restore_files(self):
        """Restore all organized files back to the main downloads folder"""
        print("🔄 Restoring files to main Downloads folder...")
        
        restored_count = 0
        
        for category_folder in self.downloads_path.iterdir():
            if category_folder.is_dir() and category_folder.name in self.file_categories:
                for file_path in category_folder.iterdir():
                    if file_path.is_file():
                        try:
                            destination = self.downloads_path / file_path.name
                            
                            # Handle name conflicts
                            counter = 1
                            while destination.exists():
                                name_parts = file_path.stem, counter, file_path.suffix
                                new_name = f"{name_parts[0]}_restored_{name_parts[1]}{name_parts[2]}"
                                destination = self.downloads_path / new_name
                                counter += 1
                            
                            shutil.move(str(file_path), str(destination))
                            restored_count += 1
                            self.logger.info(f"Restored: {file_path.name}")
                            
                        except Exception as e:
                            self.logger.error(f"Error restoring {file_path.name}: {str(e)}")
                
                # Remove empty category folder
                try:
                    if not any(category_folder.iterdir()):
                        category_folder.rmdir()
                        self.logger.info(f"Removed empty folder: {category_folder.name}")
                except:
                    pass
        
        print(f"✅ Restored {restored_count} files")


def main():
    """Main function with command-line interface"""
    print("🗂️  Downloads Folder Organizer")
    print("="*40)
    
    organizer = DownloadsOrganizer()
    
    while True:
        print("\nChoose an option:")
        print("1. 👀 Preview organization (dry run)")
        print("2. 🚀 Organize downloads folder")
        print("3. 🔄 Restore files to main folder")
        print("4. 📍 Show downloads path")
        print("5. ❌ Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n🔍 Preview Mode - Scanning files...")
            organizer.organize_downloads(dry_run=True)
            
        elif choice == '2':
            confirm = input("\n⚠️  This will move files in your Downloads folder. Continue? (y/N): ")
            if confirm.lower() in ['y', 'yes']:
                print("\n🚀 Organizing downloads folder...")
                organizer.organize_downloads(dry_run=False)
            else:
                print("❌ Operation cancelled")
                
        elif choice == '3':
            confirm = input("\n⚠️  This will restore organized files back to main folder. Continue? (y/N): ")
            if confirm.lower() in ['y', 'yes']:
                organizer.restore_files()
            else:
                print("❌ Operation cancelled")
                
        elif choice == '4':
            print(f"\n📍 Downloads folder location:")
            print(f"   {organizer.downloads_path}")
            print(f"🖥️  Operating System: {organizer.system}")
            
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Script interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        logging.error(f"Unexpected error: {str(e)}")
